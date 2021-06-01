# -*- coding: utf-8 -*-
# Date: 2021/05/12

import os

path = 'E:/Repositories/Python/阶段1-Python核心编程/代码/11-常用模块/os模块深入.py'

# 返回规范化的绝对路径：把不符合规范的 / 改成操作系统默认的格式
# path = os.path.abspath('E:/Repositories/Python/阶段1-Python核心编程/代码/11-常用模块/os模块深入.py')
# print(path)
# # 能够给 能找到的相对路径规范成绝对路径
# path = os.path.abspath('os模块深入.py')
# print(path)


# 从最后一个  / 或 \\  分割
# path = os.path.split('E:/Repositories/Python/阶段1-Python核心编程/代码/11-常用模块/os模块深入.py')
# print(path)
# path = os.path.split('E:/Repositories/Python/阶段1-Python核心编程/代码/11-常用模块')
# print(path)

# # os.path.split 的第一个元素
# ret1 = os.path.dirname('E:/Repositories/Python/阶段1-Python核心编程/代码/11-常用模块/os模块深入.py')
# # os.path.split 的第二个元素
# ret2 = os.path.basename('E:/Repositories/Python/阶段1-Python核心编程/代码/11-常用模块/os模块深入.py')
# print(ret1)
# print(ret2)

# 判断路径（问价/文件夹）是否存在
# ret = os.path.exists('E:/Repositories/Python/阶段1-Python核心编程/代码/11-常用模块/os模块深入.py')
# print(ret)

# 判断路径是不是一个绝对路径
# ret1 = os.path.isabs('os模块深入.py')
# ret2 = os.path.isabs('E:/Repositories/Python/阶段1-Python核心编程/代码/11-常用模块/os模块深入.py')
# print(ret1)
# print(ret2)

# 判断是否是一个文件夹
# ret = os.path.isdir('E:/Repositories/Python/阶段1-Python核心编程')
# print(ret)
# # 判断是否是一个文件
# ret = os.path.isfile('os模块深入.py')
# print(ret)

# ret1 = os.path.getatime(path)  # 返回path所指向的文件或者目录的最后访问时间
# ret2 = os.path.getmtime(path)  # 返回path所指向的文件或者目录的最后修改时间
# ret3 = os.path.getsize(path)  # 返回path的大小. 也可以返回文件夹的大小（至少是4096）
# print(ret1)
# print(ret2)
# print(ret3)


