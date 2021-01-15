# 爬取雪球网中的资讯
import requests
import bs4

ret1 = requests.get(
    url="https://xueqiu.com/",
    headers={
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }
)

# print(ret1.cookies.get_dict())

ret = requests.get(
    url="https://xueqiu.com/",
    headers={
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'

    },
    cookies=ret1.cookies.get_dict()
)

ret.encoding = 'utf-8'
print(ret.text)
