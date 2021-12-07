import re
from parsel import Selector

with open("listpage.html", mode="r", encoding="utf-8") as fp:
    text = fp.read()

selector = Selector(text)

for div in selector.css("div.work-list-box > div"):
    # #body > main > div.all-work-list > div > div:nth-child(1) > div.normal-card-img
    detail_url = div.css("div.card-img > a::attr(href)")
    if detail_url:
        detail_url = detail_url.extract_first()  # 详情页链接
    title = div.css("div.card-info > p.card-info-title > a::attr(title)")
    if title:
        title = re.sub(r"[🌍！#【】{}]", "", title.extract_first().strip().replace(" ", ""))
    style = div.css("div.card-info > p.card-info-type::attr(title)")
    if style:
        style = style.extract_first()
    card_info_item = div.css("div.card-info > p.card-info-item > span::text")
    if card_info_item:
        card_info_item = card_info_item.extract()
        viewCount = card_info_item[0]
        commentCount = card_info_item[1]
        recommendCount = card_info_item[2]
    username = div.css("div.card-item > span:nth-child(1) > a::attr(title)")
    if username:
        username = username.extract_first()
    publishTimeDiffStr = div.css("div.card-item > span:nth-child(2)::attr(title)")
    if publishTimeDiffStr:
        publishTimeDiffStr = re.compile(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}").\
            search(publishTimeDiffStr.extract_first()).group()
        print(publishTimeDiffStr)