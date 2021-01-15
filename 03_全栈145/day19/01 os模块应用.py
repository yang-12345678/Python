import os

'''使用python代码统计一个文件夹中所有文件的总大小'''


# 递归
def func(path):
    size_sum = 0
    name_list = os.listdir(path)
    for name in name_list:
        path = os.path.join(path, name)
        if os.path.exists(path):
            if os.path.isdir(path):
                size = func(path)
                size_sum += size
            else:
                size_sum += os.path.getsize(path)
    return size_sum


ret = func('E:\\Python')
print(ret)
