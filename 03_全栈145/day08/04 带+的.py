# 不论读取了多少内容，光标在哪，写入的时候都是在结尾写入
# 最好用的读写同时存在的模式
f = open("example.txt", "r+", encoding='utf-8')

# 先读后写
# s = f.read(3)  # 读取三个字符
# print(s)
# f.write("纳兰性德")  # r+模式强行移动光标，也是在结尾

# 先写后读
# f.write("人生若")
# s = f.read()
# print(s)
# f.close()

# 应采用先读后写
