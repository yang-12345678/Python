class Foo:
    # 类变量，在类中的函数之外
    country = '中国'

    def __init__(self, name):
        # 实例变量，在类中的函数之内
        self.name = name


'''每个对象都有属于自己的空间，各个对象空间之间互不干扰，
所有的操作都先在自己的空间中找，找不到的话在去类中找'''

a = Foo("杨")
b = Foo("张")

'''只能改 a 自己中country的值'''
# a.country = "美国"


"""准则：实例变量使用对象名访问   obj.name
       类变量使用类名访问   Foo.country    （实在不方便时，采用对象名访问）"""
'''改变类变量的值，即所有对象中country的值'''
Foo.country = "美国"


print(a.country)
print(b.country)
