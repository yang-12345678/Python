x = 1

# 使用二分法可以提高效率（有序序列才能用二分法）
# lst = [22, 33, 44, 55, 66, 77, 88, 99, 101, 238, 345, 456, 567, 678, 789]
# n = 77
#
# left = 0
# right = len(lst) - 1
# 最原始的算法
# while left < right:  # 边界，当右边比左边小的时候退出循环
#     mid = (left + right) // 2
#     if lst[mid] > n:
#         right = mid - 1
#     if lst[mid] < n:
#         left = mid + 1
#     if lst[mid] == n:
#         print("找到了这个数")
#         break
#
# else:
#     print("没有这个数")

# 2 ** n < 数据量  最多n+1次


# 递归可以完成二分法
lst = [22, 33, 44, 55, 66, 77, 88, 99, 101, 238, 345, 456, 567, 678, 789]


def func(n, left, right):
    if left <= right:
        mid = (left + right) // 2
        if n > lst[mid]:
            left = mid + 1
            return func(n, left, right)
        if n < lst[mid]:
            right = mid - 1
            # 加return，深坑
            return func(n, left, right)
        if lst[mid] == n:
            print("找到了")
            return mid  # 通过return返回，终止递归
    else:
        print("没有这个数")
        return -1  # 索引从零开始，尽量避免返回None


# 找66，从0开始找，右边界是len-1
ret = func(66, 0, len(lst) - 1)
print(ret)
