# -*- coding: utf-8 -*-
# created by Xin Li, a PhD candidate from Wuhan University
# and this is only for the purpose of scientific research or study
# 2017/10/27
# thank you

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json


class TestcrawlPipeline(object):
    def __init__(self):
        corpus_dir = 'D:\\python_projects\\testcrawl\\data\\'
        self.filehandle = codecs.open(corpus_dir + 'results.json', 'w', encoding='utf-8')
        self.filehandle.write('[')
        self.is_first_item = True

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False)
        if not self.is_first_item:
            line = ",\n" + line
        self.filehandle.write(line)
        self.is_first_item = False
        return item

    def close_spider(self, spider):
        self.filehandle.write(']')
        self.filehandle.close()
