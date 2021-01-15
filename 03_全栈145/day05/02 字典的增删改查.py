dic_ex = {'name': "alex", "age": 9000}
"""
    dict  用{}来表示   键值对数据  {key:value}
    
    键： 唯一性  不可变    字符串，数字，布尔型，元组，列表不可以，列表可变，键都是可哈希的
"""
# print(dic)
'''增'''
dic = {"易大师": "剑圣", "剑豪": "托儿所", "草丛伦": "大宝剑", '诺手': '人头狗'}
# print(dic)

dic.setdefault('火女', '安妮')
dic.setdefault('火女', '火男')
'''setdefault, 第一个参数为key，key不存在，则添加key和value；
   若key存在，则不进行任何操作
'''
print(dic)
'''删'''
# ret = dic.pop('易大师')  # 通过key删除，返回值是value
# print(ret)
# print(dic)

# del dic['剑豪']
# # dic.clear()  # 清空字典
# print(dic)
#
# ret = dic.popitem()  # 随机删除，返回元组
# print(ret)
# print(dic)

'''改'''
# dic['剑豪'] = 'hsg'
# print(dic)
#
# dic1 = {1: 2, 3: 4, 5: 6}
# dic1.update(dic)  # 存在则覆盖，不存在则添加
# print(dic1)

'''查'''
# for i in dic:  # for 循环默认是获取字典中的键
#     print(i)
#
# print(dic['易大师'])  # 键不存在则抱错
# print(dic.get('易大师'))  # 不存在则返回None，可以加  ，default，没有则返回default
'''get  获取后不能赋值'''
# print(dic.setdefault('易大师'))  # 不存在返回None

'''key value item'''  # 字典中独特的操作
# print(dic.keys())  # 高仿列表
# print(dic.values())  # 高仿列表
# print(dic.items())  # 高仿列表
# 可迭代
# for i in dic.keys():  # 获取字典的每一个键
#     print(i)

# for i in dic.values():  # 获取字典的每一个值
#     print(i)

# for i in dic.items():  # 获取字典的键值对， 以元组形式返回
#     print(i)

'''解构(解包)'''  # 将后面结构打开， 按位置赋值给变量
# a, b = [1, 2]  # 解构支持列表，元组，字符串
# print(a, b)

# dic1 = {}
# dic = dic1.fromkeys([1, 2, 3], 'abc')  # 批量创建字典, 几乎不用，返回新的字典
# print(dic)
'''字典的嵌套'''

dic1 = {
    'name': '汪峰',
    'age': 43,
    'wife': {
        'name': '国际章',
        'age': 39,
        'salary': 100000
    },
    'baby': [{
        'name': '熊大',
        'age': 18
    }, {
        'name': '熊二',
        'age': 15
    }]
}
# print(dic1['baby'][0]['age'])
