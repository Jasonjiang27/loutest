# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from githubcrawl.models import engine,Repository

class GithubcrawlPipeline(object):
    def process_item(self, item, spider):
        item['commits']=int(item['commits'])
        item['branches']=int(item['branches'])
        item['releases']=int(item['releases'])

        self.session.add(Repository(**item))
        return item
    
    def open_spider(self,spider):
        """
        爬虫开启时创建数据库session
        """
        Session = sessionmaker(bind=engine)
        self.session = Session()
        
    def close_spider(self,spider):
        self.session.commit()
        self.session.close()