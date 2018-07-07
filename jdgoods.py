# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode

from jdgoods_spider.items import JdgoodsSpiderItem




class JdgoodsSpider(scrapy.Spider):

    def __init__(self, keyword, pages):
        self.keyword = keyword
        self.pages = pages

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            keyword=crawler.settings.get('KEYWORD'),
            pages=crawler.settings.get('PAGES')
        )

    name = 'jdgoods'
    allowed_domains = ['search.jd.com']
    start_urls = ['https://search.jd.com/']

    def parse(self, response):
        goods = response.css('.gl-item')
        for good in goods:
            item = JdgoodsSpiderItem()

            good_url = good.css('div[class*=p-name]').css('a::attr(href)').extract_first()
            name = good.css('div[class*=p-name]').css('em::text').extract()
            price = good.css('.p-price').css('i::text').extract_first()
            shop = good.css('.p-shop').css('a::text').extract_first()
            shop_url = good.css('.p-shop').css('a::attr(href)').extract_first()

            item['name'] = name
            item['price'] = price
            item['shop'] = shop
            item['good_url'] = good_url
            item['shop_url'] = shop_url

            yield item

        for page in range(1, self.pages*2+1):
            data = {
                'keyword': self.keyword,
                'enc': 'utf - 8',
                'page': page,
                's': (page-1)*30
            }
            querise = urlencode(data)
            next_page_url = 'https://search.jd.com/Search?' + querise

            yield scrapy.Request(url=next_page_url, callback=self.parse)