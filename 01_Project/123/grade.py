# 打开date文件，将其中内容读入到列表ls中，用逗号替换换行符
with open('data.csv', 'r') as f1:
    ls = []
    for line in f1:
        line = line.replace("\n", "")
        ls.append(line.split(","))
    # print(ls)

    # 求出总分，平均分，给出总评， 并插入列表ls中
    for i in range(len(ls)):
        sum = 0  # 记录总分
        aver = 0

        for j in range(len(ls[i])):

            # 插入平均分表头
            if ls[i][j] == '总分':
                ls[i].insert(j + 1, "平均分")

            # 筛选分数
            if i > 0 and j > 1 and j < 8:
                sum += eval(ls[i][j])

            # 计算出sum后退出列循环，并求出aver
            if ls[i][j] == '':
                aver = sum / 6
                break
        aver = round(aver, 2)
        sum = round(float(sum), 2)
        print(sum)
        # 除表头外， 插入sum和aver
        if sum > 0:
            ls[i][j] = str(sum)
            ls[i].insert(j + 1, str(aver))
        # 判断并插入总评结果
        if i > 0:
            if aver >= 80:
                ls[i][-1] = "优秀"
            elif aver >= 60:
                ls[i][-1] = "合格"
            else:
                ls[i][-1] = "不及格"

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
                if ls_sort[i][-4] == ls_sort[i - 1][-4]:
                    ls_sort[i][-2] = ls_sort[i - 1][-2]
                else:
                    ls_sort[i][-2] = str(int(ls_sort[i - 1][-2]) + 1)

        f2.write(','.join(ls_sort[i]) + '\n')

# 查询计算机基础成绩大于80的女生名单
with open("out.csv", "w") as f3:
    # 制作表头
    ls2 = [['姓名', '性别', '计算机基础']]

    # 筛选符合条件的女生
    for ls3 in ls_sort:
        if ls3[1] == "女" and eval(ls3[2]) > 80:
            ls2.append(ls3)
    # print(ls2)

    # 写入out文件
    for i in range(len(ls2)):
        if i == 0:
            f3.write(','.join(ls2[i]) + '\n')
        else:
            f3.write(','.join(ls2[i][:3]) + '\n')
