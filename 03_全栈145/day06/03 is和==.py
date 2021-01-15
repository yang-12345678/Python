x = 1

# == 比较 比较的是值

# n = 10
# n1 = 10
#
# print(n == n1)  # True

# li1 = [1, 2, 3]
# li2 = [1, 2, 3]
# print(li1 == li2)

'''is 是 比较  比较的是内存地址'''

# i = 'alex'
# print(id(i))  # 打印的是内存地址

# n = 10
# print(id(n))

'''字符串'''
# a = 'alex'
# b = 'alex'
# print(a is b)  # True
'''数字'''
# n = 10
# n1 = 10
# print(n is n1)  # True
'''列表'''
# li = [1, 2, 3]
# li2 = [1, 2, 3]
# print(li is li2)  # False
'''元组'''
# tu = (1, 2, 3)

# tu1 = (1, 2, 3)

# print(tu is tu1)  # True   在pycharm中是True， 在python中原定是False
'''字典'''
# dic = {1: 2}
# dic1 = {1: 2}
# print(dic is dic1)  # False

"""
    小数据池
    数字：在-5~256之间，只要值相同，地址就相同
    字符串：如果有特殊字符(@,空格,加减乘除,)，内存不一样
           单个字符乘以20以内(包括20)，内存相同  在python3.8中不是20，1000都可以
"""

# n = 257
# n1 = 257
# print(n is n1)
'# 在pycharm中会有所不同'

# a = 'alex@'
# a1 = 'alex@'
# print(a is a1)
'# 在pycharm中会有不同'

a = 'a' * 1001
a1 = 'a' * 1001
print(a is a1)
# pycharm中会有不同






















