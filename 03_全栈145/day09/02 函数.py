x = 1


# def yue():
#     print("打开手机")
#     print("打开陌陌")
#     print("搜索对象")
#     print("走吧")
#     print("出发")
#     return "10086"


# # s = yue()
# # print(s)
# print(yue())

# print("去挣钱")
# yue()

# 写函数，让用户输入a和b，返回a+b的结果
# def sum():
#     a = int(input("请输入a："))
#     b = int(input("请输入b:"))
#     return a + b
#
#
# print(sum())


# def yue(tool):  # tool就是个变量，形参
#
#     print("打开手机")
#     print("打开%s" % tool)
#     print("搜索对象")
#     print("走吧")
#     print("出发")
#
#
# # 在调用的时候给出值 ： 实参
# yue("探探")


# def chi(good_food, no_good_food, drink, ice_cream):  # 形参的位置参数
#     print(good_food, no_good_food, drink, ice_cream)
#
#
# # 实参的位置参数，按照形参的位置，给形参传值  当函数的参数很多的时候，必须记住位置
# chi("法国大蜗牛", "卫龙辣条", "大白梨", "火炬")
#
# # 关键字参数  按照形参的名字给形参传值
# chi(drink='可乐', ice_cream="老冰棍", good_food="盖浇饭", no_good_food="锅包肉")
#
# # 混合参数， 位置要对
# chi("盖浇饭", "汉堡", ice_cream="火炬", drink="营养快线")


# 默认值参数
def regist(name, phone, gender='男'):

    print(name, phone, gender)


regist("阿凡提", "10086")
regist("阿凡达", "10010")
regist("阿甘", "10001")
regist("女神", "205474", "女")
