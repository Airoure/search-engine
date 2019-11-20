import json
from elasticsearch import Elasticsearch
"""
ElasticSearch的工具类，将elasticsearch库中的部分函数特化处理，以方便项目使用。
使用步骤：
第一步：使用add_index函数添加索引
第二步：使用add_index_mapping函数给索引更新mapping（搜索策略），注意index这个参数不能为空
然后就可以使用add_to_elastic函数向服务器添加数据
"""
es = Elasticsearch()

IK_MAX_WORD = 'ik_max_word'  # 极致细分
IK_SMART = 'ik_smart'  # 粒度较大


def add_index(index):
    """
    添加索引
    :param index: 要添加的索引名称
    :return: 无返回值
    """
    result = es.indices.create(index=index, ignore=400)
    for i in result:
        print(i)


def delete_index(index):
    """
    删除索引
    :param index: 要删除的索引名称
    :return:
    """
    result = es.indices.delete(index=index, ignore=[400, 404])
    for i in result:
        print(i)


def add_to_elastic(index=None, title=None, content=None, href=None, _type=None,
                   date=None):
    """
    将一个条目加入到数据库中。
    :param index: 用于该条目的索引
    :param title: 该条目的标题
    :param content: 该条目的内容，方便分词检索
    :param href: 该条目的地址
    :param _type: 该条目的类型，检索条目时使用
    :param date: 该条目的日期，最好是发布日期
    :return: 在ElasticSearch库中存放的形式，字典
    """
    data = {
        'title': title,
        'content': content,
        'href': href,
        'type': _type,
        'date': date
    }
    es.index(index=index, body=data)
    return data


def add_to_elastic(index=None, record=None):
    """
    另一种加入方法，将构建的Record类对象传入，会自动存入ElasticSearch中
    :param index: 将使用的索引值
    :param record: 包含条目所有属性的类对象
    :return: 一个包含条目所有属性的字典
    """
    data = record.to_dict()
    es.index(index=index, doc_type=record.get_type(), body=data)
    return data


def add_index_mapping(index=None, doc_type="_doc", field=['title', 'content'],
                      mapping_type='text', analyzer='ik_max_word',
                      search_analyzer='ik_max_word'):
    """
    给索引更新mapping，方便分词查询
    :param index: 要更新mapping的索引名
    :param doc_type: 文档类型
    :param field: [],指定需要分词的字段
    :param mapping_type: 'text'\'keyword'\'number'\'array'\'date'等，
        指定数据类型，这里默认为'text'类型
    :param analyzer: 指定使用的分词器，由于默认分词器汉字支持不好，使用ik分词器ik_max_word（极致细分）
    :param search_analyzer: 搜索时使用的分词器，这里默认为ik_max_word（极致细分）
    :return:
    """
    mappings = {
            'properties': {
                field[0]: {
                    'type': mapping_type,
                    'analyzer': analyzer,
                    'search_analyzer': search_analyzer
                },
                field[1]: {
                    'type': mapping_type,
                    'analyzer': analyzer,
                    'search_analyzer': search_analyzer
                },
                'date': {
                    'type': 'date',
                    'fielddata': True
                }
            }
    }
    result = es.indices.put_mapping(index=index, doc_type=doc_type,
                                    body=mappings, include_type_name=True)
    for i in result:
        print(i)


def search_from_elastic(index=None, dsl=None):
    """
    查询数据库中数据
    :param index: 索引名称
    :param dsl: 编写好的查询语句
    :return: 字典{命中条数，查询时间(以毫秒为单位)，搜索结果的Record列表}
    """
    result = es.search(index=index, body=dsl, scroll='5m', size=1000)
    li = []
    total = result['hits']['total']['value']
    time = result['took']
    scroll_id = result['_scroll_id']
    if total is not 0:
        for k in range(0, int(total/1000)+1):
            print(json.dumps(result, indent=4, ensure_ascii=False))
            if k is not 0:
                result = es.scroll(scroll_id=scroll_id, scroll='5m')
                scroll_id = result['_scroll_id']
            for i in result['hits']['hits']:
                re = None
                if i['highlight'] is None:
                    re = Record(i['_source']['type'],
                                i['_source']['title'],
                                i['_source']['href'],
                                i['_source']['date'],
                                i['_source']['content'],
                                i['_id'],
                                i['_score'])
                else:
                    re = Record(i['_source']['type'],
                                i['highlight']['title'][0],
                                i['_source']['href'],
                                i['_source']['date'],
                                i['highlight']['content'][0],
                                i['_id'],
                                i['_score'])
                li.append(re)
    results = {
        'total': total,
        'took': time,
        'list': li
    }
    return results


def higher_search(index=None, dsl=None):
    """
    高级搜索，需要用到这个py文件中的DSL类。因此，需要对dsl对象先特殊设置。
    :param index: 索引名
    :param dsl: DSL类的对象，不可为空。
    :return: 字典{命中条数，查询时间(以毫秒为单位)，搜索结果的Record列表}
    """
    if dsl is None or dsl.is_ok() is False:
        print("---dsl类对象是空的，无法执行查询！---")
        return {}
    return search_from_elastic(index, dsl.get_query())


def default_search_type(index=None, _type=None, flag=False, keyword=None):
    """
    指定一个类型名，搜索库中所有该类型的文章
    :param keyword: 关键词
    :param flag: 是否按关键词搜索指定类型下的文章
    :param index: 索引名
    :param _type: 类型名
    :return: 字典{命中条数，查询时间(以毫秒为单位)，搜索结果的Record列表}
    """
    dsl = {
        'query': {
            'bool': {
                'must': [
                    {
                        'query_string': {
                            'default_field': 'type',
                            'query': _type
                        }
                    }
                ]
            }
        },
        'sort': {
            'date': {
                'order': 'desc'
            }
        }
    }
    highlight = {
        'fields': {
            'title': {},
            'content': {}
        }
    }
    if flag:
        dsl['query']['bool']['must'].append({
            'query_string': {
                'default_field': 'title',
                'query': keyword
            }
        })
        dsl['query']['bool']['must'].append({
            'query_string': {
                'default_field': 'content',
                'query': keyword
            }
        })
        dsl['highlight'] = highlight
        print(json.dumps(dsl, indent=4, ensure_ascii=False))
    dic = search_from_elastic(index, dsl)
    li = dic['list']
    re = []
    for i in li:
        if i.get_type() == _type:
            re.append(i)
    dic['list'] = re
    return dic


def default_search(index=None, keyword=None):
    """
    默认搜索函数，默认搜索title、content字段内容。
    :param index: 索引名
    :param keyword: 关键字
    :return: 字典{命中条数，查询时间(以毫秒为单位)，搜索结果的Record列表}
    """
    dsl = {
        'query': {
            'bool': {
                'should': [
                    {
                        'query_string': {
                            'default_field': 'title',
                            'query': keyword
                        }
                    },
                    {
                        'query_string': {
                            'default_field': 'content',
                            'query': keyword
                        }
                    }
                ]
            }
        },
        'highlight': {
            'fields': {
                'title': {},
                'content': {}
            }
        },
        'sort': {
            'date': {
                'order': 'desc'
            }
        }
    }
    return search_from_elastic(index, dsl)


class Record:
    """
    将条目封装成一个类，以便直接使用
    """
    def __init__(self, _type, title, href, date, content, _id=None, score=None):
        self.type = _type
        self.title = title
        self.href = href
        self.content = content
        self.date = date
        self.id = _id
        self.score = score

    def display(self):
        print("类型："+self.type)
        print("标题："+self.title)
        print("链接："+self.href)
        print("时间：" + self.date)
        print("内容：" + self.content)

    def get_type(self):
        return self.type

    def get_href(self):
        return self.href

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_time(self):
        return self.date

    def get_id(self):
        return self.id

    def get_score(self):
        return self.score

    def to_dict(self):
        _dict = {
            'title': self.title,
            'content': self.content,
            'href': self.href,
            'type': self.type,
            'date': self.date
        }
        return _dict


class DSL:
    """
    查询语句封装类。
    """
    def __init__(self):
        self.query = {
            'query': {
                'bool': {
                    'should': [],
                    'must': [],
                    'must_not': []
                }
            }
        }
        self.ok = False

    def is_ok(self):
        return self.ok

    def get_query(self):
        if self.ok:
            return self.query
        else:
            raise DSLError('DSL语句未设置完成，不能进行查询')

    def set_query_full(self, query={}):
        self.query = query
        self.ok = True

    def set_query_should(self, should=[]):
        self.query['query']['bool']['should'] = should
        self.ok = True

    def set_query_must(self, must=[]):
        self.query['query']['bool']['must'] = must
        self.ok = True

    def set_query_must_not(self, must_not=[]):
        self.query['query']['bool']['must_not'] = must_not
        self.ok = True

    def set_query(self, should=True, must=False, must_not=False, **kwargs):
        flag = 'null'
        if should:
            flag = 'should'
        if must:
            flag = 'must'
        if must_not:
            flag = 'must_not'
        if flag is 'null':
            print("未指定查询语句类型（should、must、must_not）！")
            return self.query
        print(kwargs)
        for key, value in kwargs.items():
            data = None
            if key is 'date':
                pass
                continue
            data = {
                'query_string': {
                    'default_field': key,
                    'query': value
                }
            }
            self.query['query']['bool'][flag].append(data)
        self.ok = True

    def set_highlight(self, highlight=None):
        if highlight is None:
            pass
        pass


class DSLError(Exception):
    """
    DSL语句配套的异常错误类，在出错时抛出
    """
    def __init__(self, errorinfo):
        super().__init__(self)
        self.errorinfo = errorinfo

    def __str__(self):
        return self.errorinfo
