
from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import time
import os
import random

class MstxSpider(CrawlSpider):

    name = 'mstx'
    allowed_domain = ['home.meishichina.com']
    start_urls = ['http://home.meishichina.com/recipe-type.html']

    rules = (
        
        Rule(LinkExtractor(allow=(r'http://home.meishichina.com/recipe/\w+/$')), follow=True),
        Rule(LinkExtractor(allow=(r'http://home.meishichina.com/recipe/\w+/page/\d+/$')), follow=True),
        Rule(LinkExtractor(allow=(r'http://home.meishichina.com/recipe-\d+.html$')), callback='save_page')
    )

    def save_page(self, response):
        name = response.xpath(".//*[@id='recipe_title']/text()").extract()[0]
        print(name)
        cwd = os.getcwd() + '/data/' + 'mstx'
        if not os.path.exists(cwd):
            os.makedirs(cwd)
        with open(cwd + '/' + name + '.html', 'wb') as f:
            f.write(response.body)
        time.sleep(random.randint(0, 2))

