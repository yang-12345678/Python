import sys
import re

# sys.argv
# print(sys.argv)  # argv的第一个参数是python这个命令后面的值

# 在终端中运行
# usr = sys.argv[1]
# name = sys.argv[2]
# print(usr)

# if usr == 'wo' and name == 'ni':
#     print("登录成功")
# else:
#     exit()

# 程序员，运维人员 在命令行执行代码
# 操纵系统  input事件 阻塞 退出了CPU竞争   一般不在操作系统中放input


# sys.path
# print(sys.path)
# 模块存在文件中，（硬盘上）
# 但是在使用的时候 import  就会加载到内存中
# 一个模块能否被导入，就看sys.path中有没有这个模块所在的路径

# 自定义模块的时候还需要在关注sys.path


# sys.modules
print(sys.modules)  # 是我们导入到内存中的所有模块的名字：这个模块的内存地址
print(sys.modules['re'])


# 可以通过这种方法，使用re的方法


