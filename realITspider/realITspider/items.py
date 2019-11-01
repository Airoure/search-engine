# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RealitspiderItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    type = scrapy.Field()
    content = scrapy.Field()
    date = scrapy.Field()
