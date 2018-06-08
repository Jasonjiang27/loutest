# -*- coding:utf-8 -*-

import scrapy


class GithubRepoSpider(scrapy.Spider):
    name = 'shiyanlou-github'

    @property
    def start_urls(self):
        url_temp = "https://github.com/shiyanlou?page={}&tab=repositories"
        return (url_temp.format(i) for i in range(1,5))

    def parse(self,response):
        for repo in response.css('li.public'):
            yield { 
                    'name':repo.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first("\n\s*(.*)"),
                    'update_time':repo.xpath('.//relative-time/@datetime').extract_first()
                    }


