# def chi(good_food, no_good_food, drink, ice_cream):
#     print(good_food, no_good_food, drink, ice_cream)
#
#
# chi("盖浇饭", "腊肠", "橙汁", "火炬")

# * 表示接受位置参数的动态传参


# def chi(name, *food):
#     """ * 表示接受位置参数的动态传参,参数是food, 接受的是元组，
#         动态参数要放在最后
#     """
#     print(name + "要吃", food)
#
#
# chi("小明", "盖浇饭", "火锅", "龙虾面")
# chi("小明", "大米饭", "小米饭")
# chi("小明", "馒头")
# chi("小明")

# 关键字的动态传参
def chi(**food):
    """ 两个* 关键字的动态传参 接受的是字典 """
    print(food)


# chi("maf")  直接传参会报错
chi(good_food="狗不理", drink="可乐")

"""
   def chi(*food, **food2)  无敌传参
   顺序： 位置 *arg 默认值 **kwarg
"""