from elasticsearch import Elasticsearch

es = Elasticsearch()


def add_index(index):
    result = es.indices.create(index=index, ignore=400)
    for i in result:
        print(i)


def delete_index(index):
    result = es.indices.delete(index=index, ignore=[400, 404])
    for i in result:
        print(i)


def add_to_elastic(index=None, title=None, content=None, url=None, _type=None,
                   date=None):
    data = {
        'title': title,
        'content': content,
        'url': url,
        'type': _type,
        'date': date
    }
    es.index(index=index, doc_type=_type, body=data)


def add_index_mapping(index=None, doc_type=None, field=None,
                      mapping_type='text', analyzer='ik_max_word',
                      search_analyzer='ik_smart'):
    mapping = {
        'properties': {
            field: {
                'type': mapping_type,
                'analyzer': analyzer,
                'search_analyzer': search_analyzer
            }
        }
    }
    result = es.indices.put_mapping(index=index, doc_type=doc_type,
                                    body=mapping, include_type_name=True)
    for i in result:
        print(i)


