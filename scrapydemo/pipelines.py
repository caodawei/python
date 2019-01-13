# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import io
import requests
from scrapy.http import request
class ScrapydemoPipeline(object):
    def process_item(self, item, spider):
        # with open("d:\\project\\"+item["company"]+".txt","a+") as fs:
        #     fs.write(item["job"]+"\n\r"+item["detail"])
        return item

class ImgPipeline(object):
    def process_item(self,item,spider):
        with open("d:\\project\\"+item["filename"]+".jpg","wb") as fs:
            res=requests.get(item["src"]).content
            fs.write(res)
        