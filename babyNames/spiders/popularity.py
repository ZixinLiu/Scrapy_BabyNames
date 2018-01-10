# -*- coding: utf-8 -*-
import scrapy
from ..items import BabynamesItem


class PopularitySpider(scrapy.Spider):
    name = 'popularity'
    allowed_domains = ['ssa.gov']
    start_urls = ['https://www.ssa.gov/oact/babynames/rankchange.html']

    def parse(self, response):
        res = response.xpath("//table[@class='border']//tr/td[1]/text()").extract()
        for ele in res:
        	yield BabynamesItem(name = ele)
