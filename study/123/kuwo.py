import requests

headers = {'Referer': 'http://www.kuwo.cn/search/list?key=%E8%96%9B%E4%B9%8B%E8%B0%A6',
           'Cookie': '_ga=GA1.2.362456424.1583842445; _gid=GA1.2.953350864.1583842445; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1583842445,1583847882; _gat=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1583848465; kw_token=JNQ7VFL5K6H',
           'csrf': 'JNQ7VFL5K6H',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}


def get_music(rid, name):
    url = "http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=128kmp3&from=web&t=1583852657788&reqId=69f212d1-62e0-11ea-ad5e-575e6d12088e".format(
        rid)
    relut = requests.get(url, headers=headers).json()
    music_url = relut["url"]
    print(music_url)
    with open("D:/KuwoMusic/{}.mp3".format(name), "wb")as f:
        music = requests.get(music_url).content
        f.write(music)
        print("下载完毕")


def main():
    singer = input('输入你需要的歌手：')
    number = input("页数:")
    for i in range(1, int(number) + 1):
        # url ='http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key=%E5%91%A8%E6%9D%B0%E4%BC%A6&pn=1&rn=30&reqId=acd958b0-62d6-11ea-828f-6b4b0f2f682d'
        url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn={}&rn=30&reqId=501ac930-62ca-11ea-9b0b-f3f6d4bed533'.format(
            singer, number)
        response = requests.get(url, headers=headers).json()
        # print(url)
        # print(response)
        data = response["data"]["list"]
        for i in data:
            rid = i["rid"]
            name = i["name"]
            # print(rid)
            # print(name)
            get_music(rid, name)


main()
