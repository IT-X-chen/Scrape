pic_url_list = ['https://img.zcool.cn/community/01222b61ab08c011013e8cd081369d.jpg@1280w_1l_2o_100sh.jpg',
                'https://img.zcool.cn/community/010f7961ab08c911013e8cd0d66ef4.gif']


for url in pic_url_list:
    if ".gif" not in url.split("/")[-1]:
        print(url)