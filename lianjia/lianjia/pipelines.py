# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
#
#
# class LianjiaPipeline:
#     def process_item(self, item, spider):
#         return item
#
import logging

import pymysql
import pymongo
from .items import LianjiaItem
from loguru import logger


class MysqlPipline(object):
    def __init__(self, host, database, port, user, password):
        self.host = host
        self.database = database
        self.port = port
        self.user = user
        self.password = password

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get("HOST"),
            database=crawler.settings.get("DATABASE"),
            port=crawler.settings.get("PORT"),
            user=crawler.settings.get("USER"),
            password=crawler.settings.get("PASSWORD"),
        )

    def open_spider(self, spider):
        """连接数据库"""
        self.mysqldb = pymysql.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            charset="utf8"
        )
        logger.info("开始抓取...")
        self.cursor = self.mysqldb.cursor()

    def process_item(self, item, spider):
        """执行数据库"""
        # logger.info(item.table)
        # logger.info(item)
        if isinstance(item, LianjiaItem):
            data = dict(item)
            keys = ', '.join(data.keys())
            values = ', '.join(['%s'] * len(data))
            try:
                sql = 'insert into %s (%s) values (%s)' % (item.table, keys, values)
                self.cursor.execute(sql, tuple(data.values()))
                self.mysqldb.commit()
                logger.info(f"推送mysql:{item}")
                return item
            except Exception:
                self.mysqldb.rollback()

    def close_spider(self, spider):
        self.cursor.close()
        self.mysqldb.close()


class MongodbPipline(object):
    def __init__(self, host, mongodb, mongoport):
        self.host = host
        self.mongodb = mongodb
        self.mongoport = mongoport

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get("HOST"),
            mongodb=crawler.settings.get("MONGODB"),
            mongoport=crawler.settings.get("MONGOPORT")
        )

    def open_spider(self, spider):
        """开启mongodb数据库"""
        self.mongodlient = pymongo.MongoClient(
            host=self.host,
            port=self.mongoport
        )
        self.mongodb = self.mongodlient[self.mongodb]

    def process_item(self, item, spider):
        self.col = self.mongodb[item.collection]
        if isinstance(item, LianjiaItem):
            try:
                self.col.insert_one(dict(item))
                logger.info(f"推送mongodb:{item}")
            except Exception:
                pass
        return item

    def close_spider(self, spider):
        self.mongodlient.close()
