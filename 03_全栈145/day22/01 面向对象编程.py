class LaoGou:
    def __init__(self, name, gender, age):
        """特殊的方法，类创建实例（对象）的时候会自动执行"""
        self.n1 = name
        self.n2 = gender
        self.n3 = age

    def func(self):
        a = 10
        print(self.n1)



obj = LaoGou("老狗", "男", 20)
obj.func()
print(obj.n1)
