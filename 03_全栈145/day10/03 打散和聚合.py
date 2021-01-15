# def func(a, b):
#     """
#     计算a+b的和
#     @param a: 第一个数据
#     @param b: 第二个数据
#     @return:
#     """
#     return a + b
#
#
# print(func.__doc__)  # document文档
# print(str.__doc__)
# print(str.upper.__doc__)

# def func(*args, **kwargs):  # *args相当于一个聚合的作用
#     print(args, kwargs)
#
#
# func(1, 2, 3, 4, 5, a=6, b=7, c=8)


# def func(*food):  # * 聚合位置参数
#     print(food)
#
#
# lst = ["鸡蛋", "煎饼果子", "猪蹄"]
# # func(lst[0], lst[1], lst[2])
# func(*lst)  # *打散 把list tuple set str 进行迭代打散

# 聚合成关键字参数
def func(**kwargs):
    print(kwargs)


dic = {"name": "alex", "age": '18'}
func(**dic)  # 打散成关键字参数
