x = 1


class Foo:
    """静态方法"""

    def __init__(self, name):
        self.name = name

    # 实例方法
    def func(self):
        print(self.name)

    # 静态方法
    # 参数默认的 self 不用再加
    @staticmethod
    def display():
        print(678)


obj = Foo("刘佳琪")
obj.func()
obj.display()
# Foo.display()
