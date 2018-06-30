# -*- coding: utf-8 -*-
import json
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
            proxy = item.xpath('.//li[@class="proxy"]/*[not(self::script)]/text()').extract()
            print(proxy)
            protocol = item.xpath('.//li[@class="https"]/text()').extract()
            protocol = 'http' if len(protocol) > 0 else 'https'
            print(protocol)


