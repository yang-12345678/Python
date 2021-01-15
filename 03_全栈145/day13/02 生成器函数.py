x = 1


# def func():
#     print("hahaha")
#     yield 1  # return和yield都可以返回数据
#     print("呵呵呵")
#
#
# gen = func()  # 不会执行你的函数，拿到的时生成器
# ret = gen.__next__()  # 执行到下一个yield
# print(ret)

# yield：相当于return，就可以返回数据，但是yield不会彻底中断函数，分段执行函数
# 函数中如果有yield，这个函数就是生成器函数，此时函数名()不是执行函数，而是创建生成器


# def order():
#     ls = []
#     for i in range(10000):
#         ls.append("衣服" + str(i))
#     return ls
#
#
# ll = order()


# def order():
#     for i in range(10000):
#         yield "衣服" + str(i)
#
#
# g = order()
# ni = g.__next__()
# print(ni)
# wo = g.__next__()
# print(wo)


# send()函数  和__next__()是一样的，可以执行下一个yield，可以给上一个yield位置传值
# def func():
#     print("我是第一个")
#     a = yield 123
#     print(a)
#     print("我是第二个")
#     b = yield 456
#     print(b)
#     print("我是第三个")
#     c = yield 789
#     print(c)
#     print("我是最后一个")
#     yield 788  # 最后收尾一定是yield
#
#
# g = func()
# print(g.__next__())  # 没有上一个yield，开头必须是__next__()
# print(g.send("将饼果子"))  # 给上一个yield传值
# print(g.send("韭菜盒子"))
# print(g.send("锅包肉"))  # 最后一个yield不能传值











