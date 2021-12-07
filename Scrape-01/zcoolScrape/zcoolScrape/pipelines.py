# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
import scrapy
from uuid import uuid4
from loguru import logger
from itemadapter import ItemAdapter
from items import ZcoolscrapeItem


# class ZcoolscrapePipeline:
#     def process_item(self, item, spider):
#         return item

class MongodbPipline(object):
    def __init__(self, mongodb_uri, mongodb_port, mongodb_database):
        """
        mongodb数据库初始化配置
        :param mongodb_uri: ip
        :param mongodb_port: 端口号
        :param mongodb_database: 数据库
        """
        self.mongodb_uri = mongodb_uri
        self.mongodb_port = mongodb_port
        self.mongodb_database = mongodb_database

    @classmethod
    def from_crawler(cls, crawler):
        """读取配置文件信息"""
        return cls(
            mongodb_uri=crawler.settings.get("MONGOURI"),
            mongodb_port=crawler.settings.get("MONGOPORT"),
            mongodb_database=crawler.settings.get("MONGODB")
        )

    def open_spider(self, spider):
        """连接数据库"""

        self.client = pymongo.MongoClient(
            host=self.mongodb_uri,
            port=self.mongodb_port
        )
        self.database = self.client[self.mongodb_database]
        logger.info(f"开启数据库:{self.database}")

    def process_item(self, item, spider):
        """执行数据库"""
        """
        self.db[self.collection].update_one({
            'name': item['name']
        }, {
            '$set': dict(item)
        }, True)
        return item
        """
        if isinstance(item, ZcoolscrapeItem):
            """如果不存在就自动添加，存在就更新"""
            self.col = self.database[item.zcoolcollection]
            self.col.insert_one(dict(item))
            # self.col.update_one(
            #     {"title": item["title"]}
            #     , {"$set": dict(item)})
            logger.info(f"插入数据:{item}")
        return item

    def close_spider(self, spider):
        """关闭数据库"""
        self.client.close()
        logger.info(f"关闭数据库:{self.database}")


from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class ZcoolPipline(ImagesPipeline):
    """存图片"""
    default_headers = {
        'accept': 'image/webp,image/*,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'referer': 'https://www.zcool.com.cn/home',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }

    def get_media_requests(self, item, info):
        """下载图片"""
        if item is not None:
            for pic_url in item["pic_url_list"]:
                if ".gif" not in pic_url.split("/")[-1]:
                    yield scrapy.Request(url=pic_url, meta={'item': item},headers=self.default_headers)

    def file_path(self, request, response=None, info=None):
        """自定义文件名"""
        item = request.meta['item']
        # 设置图片的路径为  类型名称/url地址
        # 这是一个图片的url: http://pics.sc.chinaz.com/Files/pic/icons128/7065/z1.png
        # 这句代码的意思是先取出图片的url，[0]表示从列表转成字符串
        # split分割再取最后一个值，这样写是让图片名字看起来更好看一点
        # image_name = f"{item['title']}-{str(uuid4())}.jpg"
        image_name = f"{str(uuid4())}.jpg"
        return image_name
    # def item_completed(self, results, item, info):
    #     image_paths = [x['path'] for ok, x in results if ok]
    #     if not image_paths:
    #         raise DropItem("Item contains no images")
    #     item['image_paths'] = image_paths
    #     return item
