# -*- coding: utf-8 -*-
import scrapy
from ..items import BabynamesItem

class StateSpider(scrapy.Spider):
    name = 'state'
   
    def start_requests(self):
    	yield scrapy.Request(url = "https://www.ssa.gov/oact/babynames/state/", callback= self.parse)

    def parse(self, response):
        states = response.xpath("//form/select[@id='state']/option/@value").extract()
        for year in range(1960, 1965):
        	for state in states :
        		# print year
        		# print state
        		yield scrapy.FormRequest(url = "https://www.ssa.gov/cgi-bin/namesbystate.cgi", formdata={'state':str(state), 'year': str(year)}, callback = self.parse_each_page)
  
    def parse_each_page(self, response):
    	print response.url
    	res = response.xpath("//table[2]//table//tr/td[2]/text() | //table[2]//table//tr/td[4]/text()").extract()
    	for ele in res:
    		item = BabynamesItem(name = ele)
    		yield item






# //table[2]//tr/td[2]/text() | //table[4]//tr/td[2]/text()