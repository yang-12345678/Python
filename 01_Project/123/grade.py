# 打开date文件，将其中内容读入到列表ls中，用逗号替换换行符
with open('data.csv', 'r') as f1:
    ls = []
    for line in f1:
        line = line.replace("\n", "")
        ls.append(line.split(","))
    # print(ls)

    ls[0].append("名次")
    ls[0].append("平均分")
    # print(ls)
    for i in range(len(ls)):
        sum = 0  # 记录总分
        aver = 0

        for j in range(len(ls[i])):
            # 筛选分数
            if i > 0 and 1 < j < 8:
                sum += eval(ls[i][j])

            # 计算出sum后退出列循环，并求出aver
            if j == 7:
                aver = sum / 6
                break
        aver = round(aver, 2)
        sum = round(float(sum), 2)
        # print(sum)
        # print(aver)
        # 除表头外， 插入sum和aver
        if sum > 0:
            ls[i].append(str(sum))
            ls[i].append(str(aver))

# 以总分为标准 ，排序
ls_sort = sorted(ls, key=lambda x: x[-4], reverse=True)

# print(ls_sort)

# 将结果写入目标文件
with open("date_target.csv", "w") as f2:
    for i in range(len(ls_sort)):
        # 向列表ls中插入名次， 表头除外
        if i > 0:

            # 若总分相同，名次相同，依次顺延
            if i == 1:
                ls_sort[i][-2] = str(i)
            else:
                if ls_sort[i][-1] == ls_sort[i - 1][-1]:
                    ls_sort[i][-2] = ls_sort[i - 1][-2]
                else:
                    ls_sort[i][-2] = str(int(ls_sort[i - 1][-2]) + 1)

        f2.write(','.join(ls_sort[i]) + '\n')

