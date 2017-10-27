# -*- coding: utf-8 -*-
# created by Xin Li, a PhD candidate from Wuhan University
# and this is only for the purpose of scientific research or study
# 2017/10/27
# thank you

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    count = scrapy.Field()
    subject = scrapy.Field()
    xml_url = scrapy.Field()
    text_url = scrapy.Field()
    abstract = scrapy.Field()
    introduction = scrapy.Field()
    methods = scrapy.Field()
    results = scrapy.Field()
    discussion = scrapy.Field()
