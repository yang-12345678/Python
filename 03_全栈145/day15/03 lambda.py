x = 1

# def func(n):
#     return n * n
#
#
# ret = func(9)
# print(ret)

# 匿名函数, 语法： lambda 参数： 返回值
a = lambda n: n * n  # __name__的值都是lambda
ret = a(9)
print(ret)

# print(func.__name__)  # 查看函数名字
# print(a.__name__)
