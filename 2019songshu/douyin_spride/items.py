# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyinSprideItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    source_url=scrapy.Field()
    #play_url = scrapy.Field()
    image = scrapy.Field()
    tag = scrapy.Field()
    time=scrapy.Field()
    pass
