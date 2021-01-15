x = 1
# lst = ["白蛇传", "骷髅叹", "庄周闲游"]

# it = lst.__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# it = iter(lst)  # 内部封装的就是__iter__()
# print(it.__next__())
# print(it.__next__())
# print(next(it))  # 内部封装的就是__next__()
# print(dir(str))

# lst = [1, 2, 3]
# print(hash(tuple(lst)))  # 目的是为了存储，hash值尽量不要重复

# a = 10
# print(callable(a))  # 是否可以被调用执行

# print(divmod(10, 2))  # 计算商和余数

# print(round(3.5))  # 四舍五入

# print(pow(2, 4, 3))  # 求次幂，第三个参数取余数

# print(repr("你好啊\我不好"))  # 原样输出字符串

# lst = [1, 2, 3, 0]  # 水桶效应，最短的决定最终长度
# lst1 = [4, 5, 6]
# lst2 = [7, 8, 9]
# a = zip(lst, lst1, lst2)
# print("__iter__" in dir(a))
# for i in a:
#     print(i)

# s = "a = 10"
# exec(s)  # 执行代码，没有返回值，eval有返回值
# print(a)

# s = "for i in range(10): print(i)"
# c = compile(s, "", "exec")  # 第一个参数是代码段，若给出第一个，则不需要第二个（文件名），第三个参数是模式
#
# exec(c)

# s = "content = input('请输入你的名字:')"
# c = compile(s, "", "single")
#
# exec(c)
# print(content)


