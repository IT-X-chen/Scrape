import json

import requests
from urllib.parse import urlencode
# cookies = {
#     'zid': '1638679231jjYy',
#     'JSESSIONID': 'aaanmVkfLMZah65zE1-1x',
#     'sajssdk_2015_cross_new_user': '1',
#     'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2217d88e4c3c39a1-0d31a0852ea9d7-59191459-1327104-17d88e4c3c4ba0%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217d88e4c3c39a1-0d31a0852ea9d7-59191459-1327104-17d88e4c3c4ba0%22%7D',
#     'Hm_lvt_03ca55d76ee116454b60ea50024c5ba7': '1638679234',
#     'gr_user_id': '4334ea37-8759-4fb2-807c-0b4cd50b8d7b',
#     'gogouplastcourse': '1193',
#     'Hm_lpvt_03ca55d76ee116454b60ea50024c5ba7': '1638701246',
#     'r_drefresh_count': '4',
#     'z_up_bubble_count_0': '4',
#     'gr_session_id_acec0eb2dafeaf05': '6a16cc5c-e01a-42ce-ac2e-ec317f3e7391',
#     'gr_session_id_acec0eb2dafeaf05_6a16cc5c-e01a-42ce-ac2e-ec317f3e7391': 'true',
# }

headers = {
    # 'Connection': 'keep-alive',
    # 'Pragma': 'no-cache',
    # 'Cache-Control': 'no-cache',
    # 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'Upgrade-Insecure-Requests': '1',
    # 'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'Sec-Fetch-Mode': 'navigate',
    # 'Sec-Fetch-User': '?1',
    # 'Sec-Fetch-Dest': 'document',
    # 'Referer': 'https://www.zcool.com.cn/home',
    # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

# url='https://www.zcool.com.cn/home?'+urlencode({'p': '1'})
# print(url)
response = requests.get("https://www.zcool.com.cn/work/ZNTY3NDYyMTI=.html", headers=headers)
print(response.text)
# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://www.zcool.com.cn/home?p=2', headers=headers, cookies=cookies)
