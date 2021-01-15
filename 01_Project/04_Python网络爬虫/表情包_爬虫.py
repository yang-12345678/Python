# https://www.doutula.com/photo/list/
# 爬虫
'''
1、确定网址
2、发起请求
 4、保存数据
'''
import re
import requests  # 模拟浏览器获取数据的工具

# 反爬  防止机器人进行数据窃取
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
    "Referer": "https://www.doutula.com/photo/list/"
}

url = "https://www.doutula.com/photo/list/"
response = requests.get(url, headers=header).text  # .text 提取网页数据
print(response)

# response筛选 通过网址 ——》图片
# 正则表达式
gif_urls = re.findall('data-original="(.*)"', response)
# print(gif_urls)

# 依次通过网址下载图片
for url in gif_urls:
    print(url)
    # 保存文件 路径 名字
    image_name = url.split("/")[-1]

    with open("GIf/" + image_name, "wb") as f:
        f.write(requests.get(url).content)
