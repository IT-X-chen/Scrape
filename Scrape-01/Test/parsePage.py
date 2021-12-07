from parsel import Selector

with open("detail.html", mode="r", encoding="utf-8") as fp:
    text = fp.read()

selector = Selector(text)
position_info = selector.css("div.position-info > span::attr(title)")
if position_info:
    area = position_info.extract_first().split("|")[0]
    profession = position_info.extract_first().split("|")[1].strip()
    print(area)
    print(profession)
url_list = selector.css("div.work-show-box.mt-40.js-work-content > div > div > img::attr(src)")
if url_list:
    url_list = url_list.extract()
