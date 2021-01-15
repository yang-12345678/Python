import requests

'''requests模块可以模仿任何的请求'''

# 使用这个模块，去伪造发送请求
ret = requests.get(url="http://www.autohome.com.cn/news/")

# 请求返回的数据：原始的二进制数据
# print(ret.content)

# 指定编码
ret.encoding = "gbk"

# 请求返回的数据：将原始的二进制数据转换成文字
print(ret.text)
