import scrapy
import re
from urllib.parse import urljoin
from copy import deepcopy
from ..items import LianjiaItem


class LianjiaaSpider(scrapy.Spider):
    name = 'lianjiaa'  # 爬虫文件名
    allowed_domains = ['https://nj.lianjia.com']  # 允许的域名
    start_urls = ['https://nj.lianjia.com/zufang/rs/']  # 起始的ur列表

    def __init__(self):
        self.baseurl = "https://nj.lianjia.com"
        self.totalpage = 100

    def start_requests(self):
        """重新开始请求"""
        for page in range(1, int(self.totalpage) + 1):
            url = self.baseurl + f"/zufang/pg{page}/#contentList"
            # print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """解析列表页数据"""
        house_item = deepcopy(LianjiaItem())
        for div in response.css('div.content__list > div'):
            house_item["housing"] = div.css(
                "div.content__list--item--main > p:nth-child(1) > a::text").extract_first().strip()
            house_item["location"] = "-".join(
                div.css("div.content__list--item--main > p:nth-child(2) > a::text").extract())
            p2 = div.css("div.content__list--item--main > p:nth-child(2)::text").extract()
            item = [item.strip() for item in p2 if re.search(r"\w+", item.strip()) and item.strip() != "精选"]
            house_item["area"] = item[0]
            house_item["toward"] = item[1]
            house_item["housingNum"] = item[2]
            conditions=div.css("div.content__list--item--main > p:nth-child(3) > i::text")
            house_item["conditions"] = "、".join(conditions.extract()) if conditions else "无"
            house_item["average"] = f"{div.css('div.content__list--item--main > span > em::text').extract_first()}元/月"
            house_item[
                "detailUrl"] = f"{self.baseurl}{div.css('a.content__list--item--aside::attr(href)').extract_first()}"
            house_item["picUrl"] = div.css('a.content__list--item--aside > img::attr(src)').extract_first()
            yield house_item
            # print(house_item)
            # break
