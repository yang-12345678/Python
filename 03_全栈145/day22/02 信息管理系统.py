x = 1

"""
信息管理系统：
    1.用户登录
    2.显示当前用户信息
    3.查看当前用户所有的账单
    4.购买抱枕
"""


class UserInfo:

    def __init__(self):
        self.name = None

    def info(self):
        print("当前用户是：%s" % self.name)

    def account(self):
        print("当前用户%s的账单是：。。。" % self.name)

    def shopping(self):
        print("%s够购买了抱枕" % self.name)

    def login(self):
        user = input("请输入用户名：")
        pwd = input("请输入密码：")
        if user == "alex" and pwd == "sb":
            self.name = user
            while True:
                print("""
                1.查看用户信息
                2.查看用户账单
                3.购买抱枕
                """)
                num = input("请输入选择的序号：")
                if num == "1":
                    self.info()
                elif num == "2":
                    self.account()
                else:
                    self.shopping()
        else:
            print("登录失败！")


obj = UserInfo()
obj.login()