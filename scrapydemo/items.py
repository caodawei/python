# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImgItem(scrapy.Item):
    src=scrapy.Field()
    filename=scrapy.Field()
    
class ScrapydemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company = scrapy.Field()
    job = scrapy.Field()
    detail=scrapy.Field()
    address = scrapy.Field()
    intr = scrapy.Field()
