# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from shiyanlougithub.models import engine,Repository

class ShiyanlougithubPipeline(object):
    def process_item(self, item, spider):
        #增加models.py文件里Repository里面的items，连接数据库
        self.session.add(Repository(**item))
        return item

    def open_spider(self,spider):
        Session = sessionmaker(bind=engine)
        self.session=Session()
    

    def close_spider(self,spider):
        self.session.commit()
        self.session.close()
