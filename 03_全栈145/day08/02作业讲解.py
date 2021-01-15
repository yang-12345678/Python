x = 1
'''
   给出一个纯数字列表，请对列表进行升序排序
   思路：
       1.完成a和b的交换，例如，a=10, b=24 交换之后 a=24 b=10
       2.循环列表，判断a[i]和a[i+1]的大小关系，如果a[i]大于a[i+1],则进行互换，
         循环结束的时候，当前列表的最大值就会被移动到最右端
       3.重复上述操作
'''
lst = [6, 5, 7, 1, 2, 6, 4, 5]
# lst.sort()
# print(lst)
count = 0
while count < len(lst):
    i = 0
    while i < len(lst) - 1:
        if lst[i] > lst[i+1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
        i = i + 1
    count = count + 1
print(lst)

# a = 10
# b = 5
# a, b = b, a
# print(a, b)

