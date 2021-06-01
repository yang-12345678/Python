# -*- coding: utf-8 -*-
# Date: 2021/05/12
import os

'''
思路:
1.拿到这个文件夹下所有的文件夹和文件
2.是文件就取大小
3.是文件夹就打开它
'''

path = r'C:\Users\yang\Desktop\nongzuowu'

# 递归
# def func(path):
#     size_sum = 0
#     # print(os.listdir(path))
#     name_lst = os.listdir(path)
#     for name in name_lst:
#         path1 = os.path.join(path, name)
#         if os.path.isdir(path1):
#             size_sum += func(path1)
#         else:
#             size_sum += os.path.getsize(path1)
#     return size_sum
#
# print(func(path))

# 循环
# l = [path, ]
# size_sum = 0
# while (l):
#     path = l.pop()  # 默认删最后一个
#     name_lst = os.listdir(path)
#     for name in name_lst:
#         path1 = os.path.join(path, name)
#         if os.path.isdir(path1):
#             l.append(path1)  # 堆栈思想，先进后出
#         else:
#             size_sum += os.path.getsize(path1)
# print(size_sum)