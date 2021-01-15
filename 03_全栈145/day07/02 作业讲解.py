x = 1
'''
   好声音选秀大赛评委打分的时候，可以进行输入
   假设，有十个评委，让十个评委进行打分，要求分数必须大于5分，小于10分
'''
count = 1
while count <= 10:
    fen = int(input("请第%d号评委评分" % count))
    if fen < 5 or fen > 10:
        print("是不是傻")
        continue
    else:
        print("第%s评委打分为：%d" % (count, fen))
    count += 1