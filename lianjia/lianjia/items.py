# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    table = collection = "houseinformation"
    # define the fields for your item here like:
    # name = scrapy.Field()
    housing = scrapy.Field()  # 房源
    location = scrapy.Field()  # 地理位置
    area = scrapy.Field()  # 面积
    toward = scrapy.Field()  # 朝向
    housingNum = scrapy.Field()  # 几室几厅
    conditions = scrapy.Field()  # 条件
    average = scrapy.Field()  # 月租
    detailUrl = scrapy.Field()  # 详情页链接
    picUrl = scrapy.Field()  # 图片链接
    # detailUrl = scrapy.Field()  # 详情页链接
    pass


# `src_id` varchar(100) DEFAULT NULL COMMENT '唯一标识',
# `createtime` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',

# sql = """
#     CREATE TABLE `houseinformation` (
#     `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
#     `housing` varchar(30) DEFAULT NULL COMMENT '房源',
#     `location` varchar(20) DEFAULT NULL COMMENT '地理位置',
#     `area` varchar(20) DEFAULT NULL COMMENT '面积',
#     `toward` varchar(20) DEFAULT NULL COMMENT '朝向',
#     `housingNum` varchar(30) DEFAULT NULL COMMENT '几室几厅',
#     `conditions` varchar(30) DEFAULT NULL COMMENT '条件',
#     `average` varchar(20) DEFAULT NULL COMMENT '月租',
#     `detailUrl` varchar(50) DEFAULT NULL COMMENT '详情页链接',
#     `picUrl` varchar(50) DEFAULT NULL COMMENT '图片链接',
#     PRIMARY KEY (`id`)
#     ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='链家网房源信息';
# """
