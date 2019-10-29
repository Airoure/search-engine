# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import  elasticsearch

class ItspiderPipeline(object):

    def __init__(self):
        super().__init__()
        self.es = elasticsearch.Elasticsearch()
    def process_item(self, item, spider):
        if item['title']!='' and item['content']!='':
            data = {"title":item['title'],
                    'url':item['url'],
                    'create_date':item['create_date'],
                    'content':item['content']}
            self.es.index(index="it",doc_type='it',body=data)
        return item

