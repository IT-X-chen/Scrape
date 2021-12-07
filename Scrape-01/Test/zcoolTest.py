import requests

# cookies = {
#     'zid': '1638596461BDoA',
#     'JSESSIONID': 'aaaAFWu9-OxJY-SH8Z-1x',
#     'Hm_lvt_03ca55d76ee116454b60ea50024c5ba7': '1638596462',
#     'sajssdk_2015_cross_new_user': '1',
#     'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2217d83f5c832714-0cb22dd5403879-5919145b-1327104-17d83f5c833c68%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217d83f5c832714-0cb22dd5403879-5919145b-1327104-17d83f5c833c68%22%7D',
#     'event_t': '1638358099410',
#     'gr_user_id': '557bc80a-6489-4dce-a4f2-53e473732461',
#     'gr_session_id_acec0eb2dafeaf05': 'c871dc4f-2192-456d-b526-6920f2313af4',
#     'gr_session_id_acec0eb2dafeaf05_c871dc4f-2192-456d-b526-6920f2313af4': 'true',
#     'Hm_lpvt_03ca55d76ee116454b60ea50024c5ba7': '1638596713',
# }

headers = {
    # 'Connection': 'keep-alive',
    # 'Pragma': 'no-cache',
    # 'Cache-Control': 'no-cache',
    # 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    # 'Accept': 'application/json, text/javascript, */*; q=0.01',
    # 'DNT': '1',
    # 'X-Requested-With': 'XMLHttpRequest',
    # 'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.41',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Dest': 'empty',
    # 'Referer': 'https://www.zcool.com.cn/discover?cate=0&page=100&subCate=0&hasVideo=0&city=0&college=0&recommendLevel=2&sort=9',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = (
    ('cate', '0'),
    ('subCate', '0'),
    ('hasVideo', '0'),
    ('city', '0'),
    ('college', '0'),
    ('recommendLevel', '2'),
    ('sort', '9'),
    ('limit', '20'),
    ('page', '595'),
)

response = requests.get('https://www.zcool.com.cn/discover.json', headers=headers, params=params)
print(response.text)
# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://www.zcool.com.cn/discover.json?cate=0&subCate=0&hasVideo=0&city=0&college=0&recommendLevel=2&sort=9&limit=20&page=595', headers=headers, cookies=cookies)
