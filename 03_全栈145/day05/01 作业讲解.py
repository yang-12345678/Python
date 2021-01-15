"""
    lis = [2, 3, "k", ["qwe", 20, ["K1",["tt", "3", "1"], 89], "ab", "adv"]
    1、将；列表lis中的“tt”变成大写，两种方式
    2、将列表中的数字3变成字符串“100”，两种方式
    3、将列表中的字符串“1”变成数字101，用两种方式
"""
lis = [2, 3, "k", ["qwe", 20, ["K1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis[3][2][1][1] = '100'  # 方法1
# print(lis[3][2][1][1])
lis[3][2][1][1] = str(lis[3][2][1][1] + 97)
print(lis[3][2][1][1])
# 其余类似


li = ['alex', 'eric', 'rain']
'''利用下划线将列表中的每一个元素拼接成 "alex_eric_rain" '''

s = ''
for i in li:
    s = s + i + '_'
print(s[:-1])

# print("_".join(li))


'''利用for循环和range找出100以内的所有偶数并将这些偶数插入到一个新列表中'''
ls = []
for i in range(101):
    if i % 2 == 0:
        ls.append(i)
print(ls)


"""用for循环打印100~1倒叙打印"""
# for i in range(100, 0, -1):
#     print(i)

# count = 100
# while count > 0:
#     print(count)
#     count -= 1
