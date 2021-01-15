# print(dir(str))
# 可以通过dir查看xx类型的数据可以执行哪些方法，__iter__,iterable
# print(dir(list))  # __iter__
# print(dir(int))  # 没有__iter_
# iter表示获取当前对象的迭代器，所有带__iter__可以使用for循环，可迭代对象

# 可迭代对象可以使用__iter__()方法来获得迭代器
# 迭代器里面有__next__
# 迭代器里有__iter__,__next__

# 1.只能向前
# 2.几乎不占用内存，节省内存
# 3.for循环
# 惰性机制

# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# 迭代完会报错
# print(it)

# 迭代器去模拟for循环
lst = ["你好", "我好", "大家好", "都好"]
# for el in lst:  # 底层用的是迭代器
#     print(lst)
it = lst.__iter__()
# for 循环机制
while 1:
    try:
        el = it.__next__()
        print(el)
    except StopIteration:
        break

# lst = ["你好", "我好", "大家好", "都好"]
#
# it = lst.__iter__()
# print("__iter__" in dir(it))  # 判断是否可迭代
# print("__next__" in dir(it))

# # 可以通过dir判断数据是否是可迭代的，以及数据是否是迭代器

# from collections import Iterable  # 可迭代对象
# from collections import Iterator  # 迭代器
# print(isinstance(lst, Iterable))
# print(isinstance(lst, Iterator))
# print(isinstance(it, Iterable))
# print(isinstance(it, Iterator))


# ls = [1, 2, 3, 4]
# # print(dir(ls))
# it = ls.__iter__()
# print(dir(it))
# # print(dir(it))
# its = it.__iter__()
# print(dir(its))

# list(参数)把参数进行循环迭代
# lst = ["宁缺", "桑桑", "大黑马"]
# it = lst.__iter__()
# s = list(it)  # list中，一定存在for循环，一定__next__()
# print(s)

