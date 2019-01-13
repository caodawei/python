import scrapy
from scrapy.http import Request
from items import ImgItem


class img(scrapy.Spider):
    name = 'img'
    allowed_domains = ['dangdang.com']
    start_urls = [
        "http://category.dangdang.com/cp01.54.06.06.00.00-shbig.html"]
    default_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.douban.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }

    def parse(self, response):
        allpath = response.xpath('//*[@id="search_nature_rg"]/ul/li/a/img')
        for path in allpath:
            # print(path)
            src = path.xpath(".//@data-original").extract_first()
            alt = path.xpath(".//@alt").extract_first()
            # print(src)
            # print(alt)
            item = ImgItem()
            item["src"] = src
            item["filename"] = alt
            yield item
