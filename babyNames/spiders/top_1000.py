# -*- coding: utf-8 -*-
import scrapy
from ..items import BabynamesItem

class Top1000Spider(scrapy.Spider):
    name = 'top_1000'

    def start_requests(self):
    	yield scrapy.Request(url = "https://www.ssa.gov/cgi-bin/popularnames.cgi", callback= self.parse)

    def parse(self, response):
        for year in range(1880, 2017):
        	print year
        	yield scrapy.FormRequest(url = "https://www.ssa.gov/cgi-bin/popularnames.cgi", formdata={'year': str(year), 'top': '1000', 'number':''}, callback = self.parse_each_page)
  
    def parse_each_page(self, response):
    	print response.url
    	res = response.xpath("//tr/td[2]/text() | //tr/td[4]/text()").extract() 
    	for ele in res:
    		item = BabynamesItem(name = ele)
    		yield item
#