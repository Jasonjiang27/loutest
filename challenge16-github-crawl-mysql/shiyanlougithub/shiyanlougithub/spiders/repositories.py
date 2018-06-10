# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import ShiyanlougithubItem


class RepositoriesSpider(scrapy.Spider):
    name = 'repositories'
    # allowed_domains = ['github.com']
    #start_urls = ['http://github.com/']
    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self, response):
        for repo in response.css('li.public'):
            item = ShiyanlougithubItem({
                    'name':repo.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first('\n\s*(.*)'),
                    'update_time':repo.xpath('.//relative-time/@datetime').extract_first()
                    })
            yield item



