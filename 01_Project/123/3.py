with open("2.csv", "r", encoding="utf-8") as f:
    ls = []
    for line in f:
        line = line.replace("\n", "")
        ls.append(line.split(","))
    # print(ls)

nv = []
nv.append(ls[0])

for i in range(len(ls)):
    if ls[i][4] == "女":
       nv.append(ls[i])
# print(nv)

with open("targer.txt", "w", encoding="utf-8") as f1:
    for i in range(len(nv)):
        f1.write(','.join(nv[i]) + '\n')