
import scrapy
from ..items import BabynamesItem


#############################################################################
class DecadeSpider(scrapy.Spider):
	name = "decade"

	def start_requests(self):
		base_url = "https://www.ssa.gov/oact/babynames/decades/names{}s.html"
		base = 1880
		for i in range(1, 14):
			count = i * 10
			url = base_url.format(base + count)
			print "this is full url" + url
			yield scrapy.Request(url = url, callback= self.parse)

		yield scrapy.Request(url = "https://www.ssa.gov/oact/babynames/decades/century.html", callback= self.parse)



	def parse(self, response):
		names = response.xpath("(//tbody/tr/td[2]/text())[position() < last() - 1] | (//tbody/tr/td[4]/text())").extract()
		for name in names:
			item = BabynamesItem(name = name)
			yield item