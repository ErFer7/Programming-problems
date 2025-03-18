# -*- coding: utf-8 -*-

res = 0

o = input()

mat = [None] * 12
for i in range(12):

    mat[i] = [None] * 12

for i in range(12):

    for j in range(12):

        mat[i][j] = float(input())

if o == "S":

    for i in range(7, 12):

        for j in range(12 - i, i):

            res += mat[j][i]
else:

    for i in range(7, 12):

        for j in range(12 - i, i):

            res += mat[j][i] / 30.0

print("{:.1f}".format(res))