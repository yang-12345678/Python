x = 1


# def func():
#     print("我是一个小小的函数")


# a = func
# print(func)  # 地址
# func()
# a()  # a <==> func

# func = 3
# print(func)
# 函数名就是一个变量

# a = 10
# b = 20
# c = 30
# lst = [a, b, c]
# print(lst)


# def func1():
#     print("我是1")
#
#
# def func2():
#     print("我是2")
#
#
# def func3():
#     print("我是3")
#
#
# lst = [func1, func2, func3]
# # 函数名和变量一样
# for el in lst:
#     el()

# 函数名可以作为参数传递给参数
# def my():
#     print("我是my")
#
#
# def proxy(fn):  # 代理模式，装饰器
#     print("在处理之前")
#     fn()
#     print("在处理之后")
#
#
# proxy(my)  # 把函数名作为参数传递给另一个函数


# def func1():
#     print("我是func1")
#
#
# def func2():
#     print("我是func2")
#
#
# def func(fn, gn):
#     print("我是func")
#     fn()
#     gn()
#     print("哈哈哈")
#
#
# func(func1, func2)


# def func():
#     print("我是func")
#
#     def inner():
#         print("我是inner")
#
#     return inner
#
#
# # print(func())
# # ret = func()
# # ret()
# func()()

