import scrapy
from scrapy.crawler import CrawlerProcess


class BBCScienceSpider(scrapy.Spider):

    name = "bbc_science_spider"

    def start_requests(self):
        url = 'https://www.bbc.com/news/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        headline = response.xpath("//h3[contains(@class, 'gs-c-promo-heading')]/text()").extract_first()
        introduction = response.xpath("//p[contains(@class, 'gs-c-promo-summary')]/text()").extract_first()
        bbc_sci_dict[headline] = introduction
    


bbc_sci_dict = dict()

process = CrawlerProcess()
process.crawl(BBCScienceSpider)
process.start()
print(bbc_sci_dict)