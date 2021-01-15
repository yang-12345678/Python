x = 1
# 闭包，在内层函数中访问外层函数的变量
'''
   闭包的作用：
   1.可以保护变量不收侵害
   2.可以让一个局部变量常驻内存
'''


def outer():
    a = 10  # 对外界是不开放的

    def inner():
        # nonlocal a
        # a = 20
        print(a)

    return inner
    # inner()


# 仅在outer内部改变，其他不可改变


fn = outer()
fn()  # 调用的时间是不定的，为了保证正常调用，a和inner必须常驻内存


def t():
    a = 10

    def inn():
        print(a)

    print(inn.__closure__)  # None 不是闭包，


t()
