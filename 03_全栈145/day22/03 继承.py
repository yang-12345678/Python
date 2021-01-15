x = 1

"""基本使用"""

# class Base:
#     """父类"""  # 基类
#
#     def f2(self):
#         print("f2")
#
#
# class Foo(Base):
#     """子类"""  # 派生类
#
#     def f1(self):
#         print("f1")


# 原则：先在自己类中找，没有就去找父类
# obj = Foo()
# obj.f1()
# obj.f2()

# 继承目的： 为了复用， 提高代码重用性


"""python支持多继承"""


# class Base1:
#     def show(self):
#         print('Base1.show')
#
#
# class Base2:
#     def show(self):
#         print("base2.show")
#
#
# class Foo(Base1, Base2):
#     pass
#
#
# # 和 Base1 关系更近
# obj = Foo()
# obj.show()









