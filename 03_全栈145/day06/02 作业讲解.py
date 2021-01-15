a = 0
'''
    有字符串'k:1|k1:2|k2:3|k3:4'处理成字典{'k':1, 'k1':2...}
'''
# s = 'k:1|k1:2|k2:3|k3:4'
# new_s = s.split('|')
# dic = {}
# for i in new_s:
#     k, v = i.split(":")
#     dic[k] = int(v)
# print(dic)

'''
    有如下值 li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90], 将所有大于66的值保存至字典
    的第一个key中，将所有小于66的值保存至字典的第二个key中。
    即： {'k1': 大于66的所有值列表，'k2':小于66的所有值列表}
'''
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# li1 = []   # dic = {'k1':[], 'k2': []}
# li2 = []
# for i in li:
#     if i > 66:
#         li1.append(i)  # dic.setdefault('k1').append(i)
#     elif i == 66:
#         continue
#     else:
#         li2.append(i)  # dic.setdefault('k2').append(i)
# # print(dic)

'''
   输出商品列表，用户输入序号，显示用户选中的商品
   商品列表：
   goods = [
   {'name': '电脑', 'price': 1999},
   {'name': '鼠标', 'price':10}
   {'name': '游艇', 'price':20}
   {'name': '美女', 'price':998}
   ]
   要求：
   1：页面显示 序号+商品名称+商品价格，如：
       1 电脑 1999
       2 鼠标 10
       ...
   2: 用户输入选择的商品号，然后打印商品名称及价格
   3：如果用户输入的商品号有误，则提示输入错误，并重新输入
   4：如果用户输入q或Q，退出程序
'''
# goods = [
#     {'name': '电脑', 'price': 1999},
#     {'name': '鼠标', 'price': 10},
#     {'name': '游艇', 'price': 20},
#     {'name': '美女', 'price': 998},
# ]
# while 1:
#     for i in goods:
#         # good = i
#         print(goods.index(i) + 1, i['name'], i['price'])
#     str_input = input("请输入您要选择的商品序号，输入Q或q退出：")
#
#     if str_input.isdigit() and 0 < int(str_input) < len(goods):
#         i_index = int(str_input) - 1
#         print(goods[i_index]['name'], goods[i_index]['price'])
#     elif str_input == 'Q' or str_input == 'q':
#         break
#     else:
#         print("输入有误，请重新输入！")
