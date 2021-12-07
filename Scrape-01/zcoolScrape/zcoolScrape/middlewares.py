# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class ZcoolscrapeSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ZcoolscrapeDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


"""
class RandomUserAgentMiddleware(object):
    '''
    随机更换User-Agent
    '''
    def __init__(self,crawler):
        super(RandomUserAgentMiddleware, self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get('RANDOM_UA_TYPE','random')
 
    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler)
 
    def process_request(self,request,spider):
 
        def get_ua():
            return getattr(self.ua,self.ua_type)
        request.headers.setdefault('User-Agent',get_ua())
"""
"""
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import random

class EbaySpiderMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent):
        self.user_agent = user_agent

    # 从setting.py中引入设置文件
    @classmethod
    def from_crawler(cls, crawler):
        return cls(user_agent=crawler.settings.get('MY_USER_AGENT') )

    # 设置User-Agent
    def process_request(self, request, spider):
        agent = random.choice(self.user_agent)
        request.headers['User-Agent'] = agent
        print u'当前User-Agent:',request.headers['User-Agent']
"""

import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware


class RandomUserAgentDownloaderMiddleware(UserAgentMiddleware):
    """随机UA避免反爬"""
    def __int__(self, user_agent):
        # super(RandomUserAgentDownloaderMiddleware, self).__init__()
        self.user_agent = random.choice(user_agent)
        # self.type = ua_type

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user_agent=crawler.settings.get("User_Agent_List")
            # ua_type=crawler.settings.get("RANDOM_UA_TYPE", "random")
        )

    def process_request(self, request, spider):
        # def get_ua():
        #     """获取随机请求头"""
        #     return getattr(self.user_agent)
        request.headers.setdefault('User-Agent', self.user_agent)


"""
class ProxyMiddleware(object):

    def process_request(self, request, spider):
        proxy = random.choice(settings['PROXIES'])
        request.meta['proxy'] = proxy
"""

import requests


class RandomProxyDownloaderMiddleware(object):
    """随机代理"""

    def __init__(self):
        """随机请求地址"""
        # http://localhost:5555/random
        """
        PROXIES = ['https://114.217.243.25:8118',
                'https://125.37.175.233:8118',
                'http://1.85.116.218:8118']
        """
        self.proxy_url = "http://localhost:5555/random"
        self.httptype = "http://"

    def achieve_proxy(self):
        try:
            response = requests.get(url=self.proxy_url)
            if response.status_code == requests.codes.ok:
                return response.text
            return None
        except requests.exceptions.RequestException:
            return None

    def process_request(self, request, spider):
        """设置随机代理"""
        # proxy = random.choice(settings['PROXIES'])
        request.meta['proxy'] = self.httptype + self.achieve_proxy()
