x = 1
# 将列表转换成字符串，每个元素之间用指定字符链接
# s = "_".join(['高华鑫', '刘清扬', '崔元章'])
# print(s)
#
# ss = "高华鑫_刘清扬_崔元章"
# ss.split("_")
# 字符串转换成列表
"""join 中是可迭代对象"""

# lst = ["1", "2", "3", "4"]
# # lst.clear()
# new_lst = []
# for el in lst:
#     new_lst.append(el)
#
# # 循环新列表， 删除老列表
# for el in new_lst:
#     lst.remove(el)
# print(lst)
# 删除元素之后，该元素之后的元素序号自动往前提
# 需要把删除的内容记录下来， 然后循环这个记录，删除原来的列表

# lst = ["张国荣", "张铁林", "张国立", "张曼玉", "汪峰"]
# # 删掉姓张的
# zhang = []
# for el in lst:
#     if el.startswith("张"):
#         zhang.append(el)
# print(zhang)
# print(lst)
# for el in zhang:
#     lst.remove(el)
# print(lst)


"""字典有类似的坑"""
# dic = {"1": 2, "3": 4, "5": 6}
'''# 字典在迭代自身时不允许删除(改变长度)'''
# dic.clear
# lst = []
# for k in dic:
#     lst.append(k)
# for el in lst:
#     dic.pop(el)
# print(dic)






