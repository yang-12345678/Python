x = 1

# f = open("example.txt", "r", encoding='utf-8')
# s = f.read()
# read() 读取所有内容
# print(s)
# f.close()  # 如果不关闭，在下面的程序删除这个文件会报错

"""
   文件路径
   1、绝对路径   E:\\Python\\03_全栈145\\day08   或者用一个/    从磁盘的根目录寻找或从网站上找一个链接
   2、相对路径   现对于当前源代码所在的位置  ./下一层文件夹  ../上一层文件夹
"""
# f = open("example.txt", "r", encoding='utf-8')

# s = f.readline().strip()  # 一次读一行    strip默认去掉左右空格，换行 （空白）
# print(s)
# s = f.readline()  # 一次读一行
# print(s)
# f.close()

# 用循环读完所有行
# while 1:
#     s = f.readline().strip()
#     if s != '':
#         print(s)
# f.close()   # 程序不会停


# for line in f:  # 文件是一个可迭代对象，一行一行的处理数据
#     print(line.strip())
# f.close()


# f = open('拟木兰辞.txt', "w", encoding='utf-8')  # w 不存在则创建 存在则完全覆盖
# f.write("何如薄幸锦衣郎，\n比翼连枝当日愿")
# f.flush()
# f.close()

# f = open('example.txt', "a", encoding='utf-8')  # 追加写
# f.write("何如薄幸锦衣郎，\n比翼连枝当日愿。")
# f.flush()
# f.close()

# 如果处理的是非文本文件，用b模式
# f = open('123.jpg', "rb")  # 不能写encoding
# e = open("e:/123.jpg", 'wb')
# for line in f:
#     e.write(line)
# f.close()
# e.flush()
# e.close()















