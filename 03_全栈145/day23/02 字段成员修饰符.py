x = 1

"""
公有的内部外部都可以调用
前面加  __  表示该变量私有： 只有内部能访问，外部访问报错

前面加  _ 
"""

# class Foo:
#     def __init__(self, name):
#         # 私有实例变量 / 私有字段
#         self.__name = name
#         self.age = 123
#
#     def func(self):
#         # 内部调用name
#         print(self.__name)
#
#
# obj = Foo("杨梦奇")
# # 外部调用name
# # print(obj.name)
# print(obj.age)
# obj.func()


class Foo:
    __country = "中国"

    def __init__(self):
        self._a = 10
        print(self._a)

    def func(self):
        # 内部调用
        print(self.__country)
        print(Foo.__country)


# 外部调用
obj = Foo()
obj.func()
# obj.__country


# class Foo:
#
#     def __init__(self, name):
#         self.__name = name
#
#
# obj = Foo("yang")
# # 强制访问
# print(obj._Foo__name)


"""私有的变量，不仅外部无法调用，它的子类也不能调用"""


class Base(object):
    """创建类时加object,在python内部会自动继承object类，可以帮助开辟内存，，写不写是一样的"""

    __secret = "hahaha"


class Foo(Base):
    ...
    # def func(self):
    #     print(self.__secret)

# 子类不能调用父类的私有对象
# obj = Foo()
# obj.func()
