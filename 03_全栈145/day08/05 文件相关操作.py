f = open("拟木兰辞.txt", 'w', encoding='utf-8')

# for line in f:
#     print(line.strip())
# f.seek(0)
# for line in f:
#     print(line.strip())
# f.close()
f.write("何如薄幸锦衣郎，比翼连枝当日愿")
# seek()  0 表示开头  1表示当前位置 2表示结尾  第二个参数表示是从哪个位置开始偏移的（单位是字节）
f.seek(9)
# s = f.read(1)
print(f.tell())  # 以字节为单位返回光位置  utf-8汉字三个字符，英文一个字符
# print(s)
f.truncate()  # 操作时需为写模式， 不给参数则从光标位置截断，若给参数，以字节为单位截断
f.close()
