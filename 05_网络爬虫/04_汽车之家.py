import requests
from bs4 import BeautifulSoup

ret = requests.get("http://www.autohome.com.cn/news/")
ret.encoding = "gbk"

# print(ret.text)

data_object = BeautifulSoup(ret.text, "lxml")
'''
   在内部解析器有很多种，
   html.parser  默认的解析器
   lxml 效率较高
   对文本解析之后获取到的对象，以后非常方便的根据对象去获取文本信息
'''
# 获取文本信息分两步走，
'''
   取文本中找规律和特征
   用Beautifulsoup去实现规律，特征
'''
# 测试
# 获取title标签中的文本
# find的意义：去data_object中找到第一个title标签
# tag_title = data_object.find("title")
# print(tag_title.text)

# 获取div+id 为 auto-channel-lazyload-article
news_container_object = data_object.find("div", attrs={"id": "auto-channel-lazyload-article"})
# print(news_container_object)

li_list_object = news_container_object.find_all('li')

for item_object in li_list_object:
    h3_object = item_object.find('h3')
    # 找不到h3， 说明是广告位
    if not h3_object:
        continue

    print(h3_object.text)

    # print(item_object.find("p").text)
    url = item_object.find('a').get('href')
    print(url)