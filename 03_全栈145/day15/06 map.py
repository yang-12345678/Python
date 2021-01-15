x = 1

lst = [1, 4, 7, 2, 5, 8]


# 计算每个数字的平方

def func(el):
    return el ** 2


m = map(func, lst)

print("__iter__" in dir(m))

print(list(m))
