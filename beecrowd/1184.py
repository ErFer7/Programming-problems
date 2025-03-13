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

    for i in range(1, 12):

        for j in range(i):

            res += mat[i][j]
else:

    for i in range(1, 12):

        for j in range(i):

            res += mat[i][j] / 66.0

print("{:.1f}".format(res))