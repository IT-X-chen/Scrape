import requests

# cookies = {
#     'p_h5_u': '6DE11566-1629-4580-AAAB-86B772607F03',
#     'zid': '1638631184gUva',
#     'JSESSIONID': 'aaartGlT2UwCmaSTi0-1x',
#     'Hm_lvt_03ca55d76ee116454b60ea50024c5ba7': '1638631186',
#     'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2217d8607aa8446a-015c31723d3dd1-5919145b-1327104-17d8607aa8540%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%2217d8607aa8446a-015c31723d3dd1-5919145b-1327104-17d8607aa8540%22%7D',
#     'sajssdk_2015_cross_new_user': '1',
#     'event_t': '1638358099410',
#     'gr_user_id': 'f50eaf0a-f46a-42a8-a920-f3111721b98b',
#     'gr_session_id_acec0eb2dafeaf05': '6d516240-7f45-464f-abe2-4329baf88bfd',
#     'gr_session_id_acec0eb2dafeaf05_6d516240-7f45-464f-abe2-4329baf88bfd': 'true',
#     'Hm_lpvt_03ca55d76ee116454b60ea50024c5ba7': '1638631388',
#     'r_drefresh_count': '2',
#     'z_up_bubble_count_0': '2',
# }

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.41',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.zcool.com.cn/discover?cate=0&page=100&subCate=0&hasVideo=0&city=0&college=0&recommendLevel=2&sort=9',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

response = requests.get('https://www.zcool.com.cn/work/ZNTU0NzA4MDA=.html', headers=headers)
print(response.text)
