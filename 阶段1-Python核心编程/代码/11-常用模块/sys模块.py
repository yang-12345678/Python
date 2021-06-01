# -*- coding: utf-8 -*-
# Date: 2021/05/12

import sys

# sys 是和 python 解释器打交道的

# sys.argv

'''
argv 返回值的第一个参数是python命令后面的值  这里是绝对路径，终端里可以是相对路径
python 命令指的是终端里的python执行命令

>> python 阶段1-Python核心编程\\代码\\11-sys模块\\sys模块.py 123 456 789

['阶段1-Python核心编程\\代码\\11-sys模块\\sys模块.py', '123', '456', '789']
'''
# print(sys.argv)

# usr = input("username:")
# pwd = input("password:")

# 操作系统 input 事件，阻塞程序运行，退出了 cpu 的竞争
# usr = sys.argv[1]
# pwd = sys.argv[2]
# if usr == 'yang' and pwd == '227229':
#     print('登陆成功!')
# else:
#     exit()


# sys.path

'''
模块是存在文件里的，也可以说是存在硬盘上的。
但是在使用的时候，模块被 import,这个模块就到了内存中

一个模块能否被顺利的导入 全看 sys.path 中有没有这个模块所在的路径
注：pycharm 中打开的项目目录也会在其中，但是不算数,如果在终端中运行，则不会显示

自定义模块的时候，导入模块的时候，还需要再关注 sys.path
'''
# print(sys.path)


# sys.modules
import re

# 导入到内存中所有的模块的名字：这个模块的内存地址
print(sys.modules)
print(sys.modules['re'])
print(re)