'''
前面的课程已省略，从元组开始
'''
# print((3))  # 一个元素不能构成元组
# tu = (3,)  # 元组中一个元素时不能省略逗号
# tu = tuple()  # 空元组只能这么写
# print(type(tu))

# tu = ("人民币", "美元", "英镑", "欧元")
# tu[0] = "日元"
# 元组不可变，增删改都不可
# print(tu[2])
# print(tu[::2])
# 索引可以用，切片也可以
# for el in tu:
# print(el)
# 遍历可以

# 元组第一层子元素不可改变， 但可以为任意类型（内部元素不做要求）
tu = (1, "hello", "how are you", [])
tu[3].append("峰哥")
print(tu)

a = 1,
print(type(a))
ls = [1, 3, 4]
print(ls[-1:])