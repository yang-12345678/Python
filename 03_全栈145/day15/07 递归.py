import os

x = 1


# 递归深度：自己调用自己的次数，官方深度是1000，但是在1000之前就会报错
# count = 1
#
#
# def func():
#     global count
#     print("alex是很帅的", count)
#
#     count += 1
#     func()
#
#
# func()

# 遍历 E:/Python,打印出所有的文件和普通文件名
def func(filepath, n):
    files = os.listdir(filepath)  # 查看当前目录中的文件
    for file in files:
        # 获取每一个文件的路径
        file_p = os.path.join(filepath, file)

        if os.path.isdir(file_p):  # 判断file_P是否是一个文件夹
            print("\t" * n, file)
            func(file_p, n + 1)
        else:
            print("\t" * n, file)

        # print(file)
        # print(file_p)


func("E:/Python", 0)
