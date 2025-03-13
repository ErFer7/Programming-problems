# -*- coding: utf-8 -*-

n, m = map(int, input().split())

mat = []
checkList = []

for _ in range(n):

    line = list(map(int, input().split()))

    mat.append(line)
    checkList.append(sum(line))

for i in range(m):

    checkList.append(0)
    for j in range(n):

        checkList[-1] += mat[j][i]

print(max(checkList))