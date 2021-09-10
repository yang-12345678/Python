# -*- coding: utf-8 -*-
# Date: 2021/09/09

with open("1.csv", "r") as f:
    ls = []
    for line in f:
        line = line.replace("\n", "")
        ls.append(line.split(","))

start = 0
end = 0
length = [0, 0, 0]
for i in range(1, len(ls)):

    for j in range(2, len(ls[i])):
        if ls[i][j] == "0":
            ...
        else:
            ls[i][j] = "1"


with open("1_target.csv", "w") as f2:
    for i in range(len(ls)):
        f2.write(','.join(ls[i]) + '\n')
