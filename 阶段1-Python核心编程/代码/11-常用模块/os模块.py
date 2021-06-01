# -*- coding: utf-8 -*-
# Date: 2021/05/12

import os
# os 是和操作系统交互的模块
'''创建文件夹'''
# os.makedirs('dir1/dir2')  # 创建多级目录
# os.mkdir('dir3')  # 只能创建单级目录
# os.mkdir('dir3/dir4')

'''删除文件夹：两个都只能删空文件夹'''
# os.rmdir('dir3/dir4')  # 删除一个文件夹
# os.removedirs('dir3/dir4')  # 删除多个文件夹
# os.removedirs('dir1/dir2') # 只能删空文件夹

# print(os.stat(r'E:\Repositories\Python\阶段1-Python核心编程\代码\11-常用模块\os模块.py'))

'''拼接路径'''
# print(os.listdir("E:\Repositories\Python\阶段1-Python核心编程"))
# file_lst = os.listdir("E:\Repositories\Python\阶段1-Python核心编程")
#
# for path in file_lst:
#     # new_path = '\\'.join(["E:\Repositories\Python\阶段1-Python核心编程", path])
#     # print(new_path)
#
#     # 可跨平台使用
#     new_path = os.path.join("E:\Repositories\Python\阶段1-Python核心编程", path)
#     print(new_path)

'''
执行操作系统命令

exec/eval 执行的是字符串数据类型的 python代码
os.system/os.popen 执行的是字符串数据类型的 命令行代码
'''
# os.system('dir')  # 无返回值，适合做实际操作

# ret = os.popen('dir')  # 有返回值，适合做查看类的操作
# # print(ret.read())
# s = ret.read()
# print(s.split('\n'))

print(os.getcwd())  # 获取当前工作目录
# 并不是指当前文件所在的目录，而是指当前文件是在哪个目录下执行的
# os.chdir() # 无论当前目录在哪，都切换到这个目录