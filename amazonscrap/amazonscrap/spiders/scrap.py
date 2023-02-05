import scrapy
from selenium import webdriver

class AmazonProductSpider(scrapy.Spider):
    name = "samsung_device"
    start_urls = [
        'https://www.amazon.com/s?k=samsung&page={pageno}'
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pageno = 1

    def parse(self, response):
        for product in response.css('div.s-result-item'):
            yield {
                'Device Name': product.css('span.a-text-normal::text').get(),
                'price': product.css('span.a-price-whole::text').get(),
                'Rating': product.css('span.a-size-base::text').get(),
                'Stars': product.css('span.a-size-base::text').get(),
                
            }
        next_page = response.css('a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator::text')
        print("8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888")
        print(next_page)
        print("8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888")
        
        
        if self.pageno < 10:
            self.pageno += 1
            next_page = 'https://www.amazon.com/s?k=samsung&page={pageno}'.format(pageno=self.pageno)
            yield response.follow(next_page, callback=self.parse)




       