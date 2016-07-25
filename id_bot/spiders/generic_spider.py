import scrapy
from scrapy.selector import Selector

class GSpider(scrapy.Spider):
    name = "generic"
    allowed_domains = ["ADD_DOMAINS"]
    start_urls = [
        "ADD_SPIDERS"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'

	sel = Selector(response)
        results = sel.xpath("//*[contains(@id, 'ADD_SEEK_ID')]")

        with open(filename, 'wb') as f:
        	for result in results:
			f.write(result.extract())
