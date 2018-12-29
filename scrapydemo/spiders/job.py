# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from items import ScrapydemoItem


class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/020000,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def parse(self, response):
        items = response.css("p.t1 span a::attr(href)").extract()
        for item in items:
            yield Request(item, self.parseDetail)


    def parseDetail(self, response):
        item = ScrapydemoItem()
        job = response.xpath(
            '//div[@class="cn"]/h1/text()').extract_first().strip()
        item["job"] = job
        comp = response.xpath(
            '//div[@class="cn"]/p[@class="cname"]/a[@class="catn"]/text()').extract_first().strip()
        item["company"] = comp
        
        details=response.css('div.tCompany_main>div:nth-of-type(1) *::text').extract()   
        text=""     
        for detail in details:
            text+=detail.strip()
        item["detail"]=text
        text=""
        addresses=response.css('div.tCompany_main>div:nth-of-type(2) *::text').extract()        
        for address in addresses:
            text+=address.strip()
        item["address"]=text
        
        intrs=response.css('div.tCompany_main>div:nth-of-type(3) *::text').extract()
        text=""       
        for intr in intrs:
            text+=intr.strip()
        item["intr"]=text
        return item
        
