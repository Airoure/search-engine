from elasticsearch import Elasticsearch

es = Elasticsearch()


def addIndex(index):
    result = es.indices.create(index=index, ignore=400)
    for i in result:
        print(i)


def deleteIndex(index):
    result = es.indices.delete(index=index, ignore=[400, 404])
    for i in result:
        print(i)


def addToElastic(index=None, title=None, content=None, url=None, _type=None, date=None):
    data = {
        'title': title,
        'content': content,
        'url': url,
        'type': _type,
        'date': date
    }
    es.index(index=index, doc_type=_type, body=data)


