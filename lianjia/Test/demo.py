# -*- encoding: utf-8 -*-

"""
@File    :   demo.py    
2021/11/27 11:22     Xchen~      
"""

import re
from parsel import Selector

with open('1.html',mode="r",encoding="utf-8") as fp:
    text = fp.read()

selector = Selector(text)

class BaseSettings(object):
    """读取配置文件"""

    def __init__(self, host, database, port, user, password, mongodb, mongoport):
        self.host = host
        self.database = database
        self.port = port
        self.user = user
        self.password = password
        self.mongodb = mongodb
        self.mongoport = mongoport

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get("HOST"),
            database=crawler.settings.get("DATABASE"),
            port=crawler.settings.get("PORT"),
            user=crawler.settings.get("USER"),
            password=crawler.settings.get("PASSWORD"),
            mongodb=crawler.settings.get("MONGODB"),
            mongoport=crawler.settings.get("MONGOPORT")
        )



for div in selector.css('div.content__list > div'):
    housing = div.css("div.content__list--item--main > p:nth-child(1) > a::text").extract_first().strip()
    location = div.css("div.content__list--item--main > p:nth-child(2) > a::text").extract()
    location = "-".join(location)
    p2= div.css("div.content__list--item--main > p:nth-child(2)::text").extract()
    item = [item.strip() for item in p2 if re.search(r"\w+",item.strip()) and item.strip() !="精选"]
    area = item[0]
    toward = item[1]
    housingNum = item[2]
    conditions = div.css("div.content__list--item--main > p:nth-child(3) > i::text").extract()
    price = div.css("div.content__list--item--main > span > em::text").extract_first()
    price = f"{price}元/月"
    detailUrl = "https://nj.lianjia.com"+div.css("a.content__list--item--aside::attr(href)").extract_first()
    item ={
            "housing":housing,
            "location":location,
            "area":area,
            "toward":toward,
            "housingNum":housingNum,
            "conditions":conditions,
            "price":price,
            "detailUrl":detailUrl

    }
    print(item)


