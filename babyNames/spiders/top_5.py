# -*- coding: utf-8 -*-
import scrapy
from ..items import BabynamesItem

class Top5Spider(scrapy.Spider):
    name = 'top_5'
    allowed_domains = ["ssa.gov"]
    start_urls = ["https://www.ssa.gov/OACT/babynames/top5names.html"]

    def parse(self, response):
        list = response.xpath("//tr/td[position() > 1]/text()").extract()
        for ele in list:
        	item = BabynamesItem(name = ele)
        	yield item


