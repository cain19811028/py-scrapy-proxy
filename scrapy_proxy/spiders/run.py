# -*- coding: utf-8 -*-
import base64
import scrapy
from scrapy import Request

class ProxyList(scrapy.Spider):

    name = "proxy_list"
    allowed_domains = ["proxy-list.org"]

    def start_requests(self):

        for i in range(1, 4):
            print(i)
            yield Request('https://proxy-list.org/english/index.php?p=%s' % i)

    def parse(self, response):

        list = response.xpath('//div[@class="table-wrap"]//ul')
        for item in list:
            proxy = item.xpath('.//li[@class="proxy"]//script').extract()[0]
            proxy = base64.b64decode(proxy.split("'")[1])
            print(proxy)
            protocol = item.xpath('.//li[@class="https"]/text()').extract()
            protocol = 'http' if len(protocol) > 0 else 'https'
            print(protocol)

