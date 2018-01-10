# -*- coding: utf-8 -*-
import scrapy
from ..items import BabynamesItem


class StateTop5Spider(scrapy.Spider):
    name = 'state_top_5'
 
    def start_requests(self):
		base_url = "http://www.ssa.gov/oact/babynames/state/top5_{}.html"
		for i in range(1980, 2017):
			print i
			url = base_url.format(i)
			print "this is full url" + url
			yield scrapy.Request(url = url, callback= self.parse)

    def parse(self, response):
 
        names = response.xpath("//table/tr/td[2]/text() |  //table/tr/td[4]/text() | //table/tr/td[6]/text() | //table/tr/td[8]/text() | //table/tr/td[10]/text()").extract()
        for name in names:
			item = BabynamesItem(name = name)
			yield item

