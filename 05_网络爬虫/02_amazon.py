import requests

res = requests.get(
    url="https://www.amazon.com/-/zh/gp/offer-listing/B0815JJQQ8/ref=dp_olp_NEW_mbc",
    params={"ie": "UTF8", "condition": "NEW"},
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }
)

'''可能会因为访问频率被限制（所有电商平台），可采用代理IP的机制来破解'''
print(res.text)
