# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZcoolscrapeItem(scrapy.Item):
    zcoolcollection = "zcool"
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 标题
    style = scrapy.Field()  # 种类类型
    viewCount = scrapy.Field()  # 观看数
    commentCount = scrapy.Field()  # 评论数
    recommendCount = scrapy.Field()  # 点赞数
    username = scrapy.Field()  # 点赞数
    publishTimeDiffStr = scrapy.Field()  # 发布时间
    area = scrapy.Field()  # 地区
    profession = scrapy.Field()  # 职业
    pic_url_list = scrapy.Field()  # 图片链接
    detailUrl = scrapy.Field()  # 详情页链接
    pass
