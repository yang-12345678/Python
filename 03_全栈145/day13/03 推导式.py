x = 1

# lst = []
# for i in range(1, 16):
#     lst.append(i)
# print(lst)

# 推导式：用一句话生成一个列表
# lst = [i for i in range(1, 16)]
# print(lst)
# 语法：[结果 for循环 判断]

# lst = [i for i in range(100) if i % 2 == 1]
# print(lst)

# [1, 2, 3, 4] => {0:1, 1:1, 2:2, 3:3}
# lst = [1, 2, 3, 4]
# dic = {i: lst[i] for i in range(len(lst)) if i < 2}
# print(dic)

# 语法：{k:v for循环  条件筛选}


# dic = {"jj": "林俊杰", "jay": "周杰伦", "zs": "赵四", "ln": "刘能"}
# d = {v:k for k, v in dic.items()}
# print(d)

# s = {i for i in range(100)}
# print(s)

# 集合推导式
lst = [1, 1, 2, 4, 5, 5, 53, 2, 2]
s = {i for i in lst}
print(s)
