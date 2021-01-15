# a = 10  # 全局名称空间中的内容
#
#
# def fn():  # fn也在全局名称空间
#     b = 20  # 局部名称空间  每次调用后释放内存
#     print(a)
#
#
# def gn():
#     print(a)
#
#
# fn()
# gn()

# 1.内置 2.全局 3.局部（函数调用）
# 全局作用域
# 局部作用域


# a = 10  # 全局
#
#
# def fn():
#     b = 20  # 局部
#
#     def gn():  # 局部
#         pass
#
#     print(globals())  # 查看全局作用域中的内容
#     print(locals())  # 查看当前作用域中的内容
#
#
# fn()

# a = 10
#
#
# def func():
#     global a  # 把全局中的内容引入到函数内部  相当于在全局创建一个变量
#     # a = 20  # 局部变量在函数中起作用
#     print(a)
#
#
# func()
# print(a)

def outer():
    a = 10

    def inner():
        nonlocal a  # 找最近外层层有该变量的那一层，直到找到最后一层，不会找全局，找不到则报错
        a = 20


    inner()
    print(a)


outer()
