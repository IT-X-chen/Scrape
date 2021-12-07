import logging

import scrapy
import re
from urllib.parse import urlencode
from copy import deepcopy
from items import ZcoolscrapeItem
from loguru import logger


class ZcoolSpider(scrapy.Spider):
    name = 'zcool'
    allowed_domains = ['www.zcool.com.cn']
    # start_urls = ['http://https://www.zcool.com.cn//']
    MAX_PAGE = 100
    BASE_URL = 'https://www.zcool.com.cn/home?'

    def start_requests(self):
        """构造新请求"""
        for page in range(1, self.MAX_PAGE + 1):
            url = self.BASE_URL + urlencode({'p': str(page)})
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        """解析列表页"""
        # 深拷贝
        item = deepcopy(ZcoolscrapeItem())
        for div in response.css("div.work-list-box > div"):
            detail_url = div.css("div.card-img > a::attr(href)")
            if detail_url:
                item["detailUrl"] = detail_url.extract_first()  # 详情页链接
            title = div.css("div.card-info > p.card-info-title > a::attr(title)")
            if title:
                item["title"] = re.sub(r"[🌍！#【】{}]", "", title.extract_first().strip().replace(" ", ""))
            style = div.css("div.card-info > p.card-info-type::attr(title)")
            if style:
                item["style"] = style.extract_first()
            card_info_item = div.css("div.card-info > p.card-info-item > span::text")
            try:
                if card_info_item:
                    card_info_item = card_info_item.extract()
                    item["viewCount"] = card_info_item[0]
                    item["commentCount"] = card_info_item[1]
                    item["recommendCount"] = card_info_item[2]
            except IndexError as e:
                continue
            username = div.css("div.card-item > span:nth-child(1) > a::attr(title)")
            if username:
                item["username"] = username.extract_first()
            publishTimeDiffStr = div.css("div.card-item > span:nth-child(2)::attr(title)")
            try:
                if publishTimeDiffStr:
                    item["publishTimeDiffStr"] = re.compile(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}"). \
                        search(publishTimeDiffStr.extract_first()).group()
            except AttributeError as e:
                continue
            yield scrapy.Request(url=item["detailUrl"], meta={"item": item}, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        """解析详情页"""
        # print(response.meta['item'])
        item = response.meta['item']
        position_info = response.css("div.position-info > span::attr(title)")
        if position_info:
            item["area"] = position_info.extract_first().split("|")[0]
            item["profession"] = position_info.extract_first().split("|")[1].strip()
        url_list = response.css("div.work-show-box.mt-40.js-work-content > div > div > img::attr(src)")
        if url_list:
            item["pic_url_list"] = url_list.extract()
        yield item
