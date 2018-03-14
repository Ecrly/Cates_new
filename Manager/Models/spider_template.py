import os
import scrapy.cmdline as cmd



template = \
"""
from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import time
import os
import random
import scrapy.cmdline as cmd

class MstxSpider(CrawlSpider):

    name = '%s'
    allowed_domain = ['%s']
    start_urls = ['%s']

    rules = (
        %s
    )

    def save_page(self, response):
        name = response.xpath("%s/text()").extract()[0]
        print(name)
        cwd = os.getcwd() + '/data/' + '%s'
        if not os.path.exists(cwd):
            os.makedirs(cwd)
        with open(cwd + '/' + name + '.html', 'wb') as f:
            f.write(response.body)
        time.sleep(random.randint(0, 2))

cmd.execute("scrapy crawl %s".split())


"""

args = (
    'mstx',
    'home.meishichina.com',
    'http://home.meishichina.com/recipe-type.html',
    '''
        Rule(LinkExtractor(allow=(r'http://home.meishichina.com/recipe/\w+/$')), follow=True),
        Rule(LinkExtractor(allow=(r'http://home.meishichina.com/recipe/\w+/page/\d+/$')), follow=True),
        Rule(LinkExtractor(allow=(r'http://home.meishichina.com/recipe-\d+.html$')), callback='save_page')
    ''',
    ".//*[@id='recipe_title']",
    'mstx'
)

# args = (
#     'msj',
#     'www.meishij.net',
#     'http://www.meishij.net/chufang/diy/',
#     '''
#         Rule(LinkExtractor(allow=(r'http://www.meishij.net/china-food/xiaochi/$')), follow=True),
#         Rule(LinkExtractor(allow=(r'http://www.meishij.net/china-food/xiaochi/\?&page=\d+$')), follow=True),
#         Rule(LinkExtractor(allow=(r'http://www.meishij.net/zuofa/\w+\.html')), callback='save_page')
#     ''',
#     ".//*[@id='tongji_title']",
#     'msj',
# )
#
# temp = template % args
# with open(os.getcwd() + '/spiders/' + 'Spider_mstx.py', 'w') as f:
#     f.write(temp)
#
# cmd.execute("scrapy crawl mstx".split())



