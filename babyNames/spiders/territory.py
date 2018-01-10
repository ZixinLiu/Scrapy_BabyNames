# -*- coding: utf-8 -*-
import scrapy
from ..items import BabynamesItem


class TerritorySpider(scrapy.Spider):
    name = 'territory'

    def start_requests(self):
		PR_url = "https://www.ssa.gov/oact/babynames/territory/puertorico{}.html"
		other_url = "https://www.ssa.gov/oact/babynames/territory/allother{}.html"
		for i in range(1998, 2017):
			PR_f_url = PR_url.format(i)
			other_f_url = other_url.format(i)
			print "this is full PR url" + PR_f_url
			print "this is full other url" + other_f_url
			yield scrapy.Request(url = PR_f_url, callback= self.parse)
			yield scrapy.Request(url = other_f_url, callback= self.parse)


    def parse(self, response):
    	res = response.xpath("//table/tr/td[2]/table//tr/td[2]/text() | //table/tr/td[2]/table//tr/td[4]/text()").extract()
    	for name in res:
			item = BabynamesItem(name = name)
			yield item

