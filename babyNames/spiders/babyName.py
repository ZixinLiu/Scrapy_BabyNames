# -*- coding: utf-8 -*-
import scrapy
from ..items import BabynamesItem

#############################################################################
class BabynameSpider(scrapy.Spider):
    name = 'babyName'

    def start_requests(self):
        with open('data/links.txt') as links:
            for link in links:
                yield scrapy.Request(url=link, callback=self.parse)

    def parse(self, response):
    	dataList = NameExtractor().parse(response)
    	for name in dataList:
    		item = BabynamesItem(name = name)
        	yield item

#############################################################################
class NameExtractor():
    def __init__(self):
        pass

    def parse(self, response):
         return response.xpath("//tbody/tr/td[3]/text() | //tbody/tr/td[2]/text()").extract()



