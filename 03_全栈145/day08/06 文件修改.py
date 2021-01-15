# 文件不支持直接修改
# 打开目标文件
# 读取内容
# 将修改后的写入新的副本
# 重命名副本
import os

import time

with open("1234", "r", encoding='utf-8') as f1, \
        open("1234_副本", 'w', encoding='utf-8') as f2:
    for line in f1:
        line = line.replace('alex', 'sb')
        f2.write(line)

# 删除文件
os.remove("1234")
time.sleep(3)
os.rename("1234_副本", "1234")