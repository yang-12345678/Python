import json

# dic = {'1': '2', '3': '4'}
# ret = json.dumps(dic)
# print(dic, type(dic))
# print(ret, type(ret))
# # 序列化  转成字符串的过程
#
#
# # 反序列化  从字符串返回到其他数据类型
# res = json.loads(ret)
# print(res, type(res))

'''# 问题1   会把数字转换成字符串'''
# dic = {1: '2', 3: '4'}
# ret = json.dumps(dic)
# print(dic, type(dic))
# print(ret, type(ret))
#
# res = json.loads(ret)
# print(res, type(res))


'''# 问题2  列表没变，元组变了列表'''
dic = {1: [1, 2, 3], 2: (4, 5, 'aa')}
ret = json.dumps(dic)
print(dic, type(dic))
print(ret, type(ret))

res = json.loads(ret)
print(res, type(res))


'''# 问题3'''
# s = {1, 2, 'aa'}
#
# ret = json.dumps(s)
# print(s, type(s))
# print(ret, type(ret))
#
# res = json.loads(ret)
# print(res, type(res))


'''# 问题4  TypeError:keys must be str, int, float, bool or None, not tuple'''
# json.dumps({(1, 2, 3): 123})

# json  在所有的语言中都通用： json序列化的数据  在python上序列化了， 在java上也可以反序列化
# json能够处理的数据类型是非常有限的： 字符串， 列表， 字典， 数字
# 字典中的key只能是字符串  不支持元组，  其他可以转换成字符串

# 后端语言： java  c  c++  c#
# 前端语言： 在网页上展示


# 向文件当中记录字典
# dic = {'1': '2', '3': '4'}
# ret = json.dumps(dic)  # 在内存中加载成字符串
# with open('json_file', 'a') as f:
#     f.write(ret)

# 从文件中读取字典  自己向文件中添加内容，必需是双引号
# with open('json_file', 'r') as f:
#     str_dic = f.read()
#
# dic = json.loads(str_dic)
# print(dic.keys())

# dump load  直接操作文件的   dumps和loads 是操作内存的
# dic = {'1': '2', '3': '4'}
# # ret = json.dumps(dic)
# with open('json_file', 'a') as f:
#     json.dump(dic, f)

# with open('json_file', 'r') as f:
#     dic = json.load(f)
# print(dic.keys())

'''# 问题五，可以多次dump， 但不能多次load'''


'''需求：就是想把一个一个的字典放到文件中， 再一个一个的取出来'''
dic = {'1': '2', '3': '4'}

# with open('json_file', 'a') as f:
#     str_dic = json.dumps(dic)
#     f.write(str_dic + '\n')
#     str_dic = json.dumps(dic)
#     f.write(str_dic + '\n')
#     str_dic = json.dumps(dic)
#     f.write(str_dic + '\n')

# with open('json_file', 'r') as f:
#     for line in f:
#         dic = json.loads(line.strip())
#         print(dic.keys())


# json  所有语言都通用， 只支持列表，字典，字符串，和数字
# key 必需是字符串
# dumps loads   在内存中做数据转换
# dump load    直接将数据类型写入文件/读出
