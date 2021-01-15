x = 1


# 没有元组推导式，生成器表达式
# tu = (i for i in range(10))
# print(tu)  # 生成器
# print(tu.__next__())
# print(tu.__next__())

def func():
    print(111)
    yield 222


g = func()
g1 = (i for i in g)
g2 = (i for i in g1)
print(list(g))  # 从源头把数据拿走了
print(list(g1))  # 后面都没有值了
print(list(g2))
