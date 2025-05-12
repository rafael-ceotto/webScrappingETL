import scrapy


class LaptopSpider(scrapy.Spider):
    name = "laptop"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/notebook#D[A:notebook]"]
    page_count = 1
    max_page = 10

    def start_requests(self):
        url = 'https://lista.mercadolivre.com.br/notebook'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        products = response.css('div.ui-search-result__wrapper')

        for product in products:
            yield {
                'brand': product.css('span.poly-component__brand::text').get(),
                'name': product.css('a.poly-component__title::text').get()
            }

        pass
