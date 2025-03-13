# -*- coding: utf-8 -*-

res = 0

line = int(input())
o = input()

mat = [None] * 12
for i in range(12):

    mat[i] = [None] * 12

for i in range(12):

    for j in range(12):

        mat[i][j] = float(input())

if o == "S":

    for i in range(12):

        res += mat[line][i]
else:

    for i in range(12):

        res += mat[line][i] / 12.0

print("{:.1f}".format(res))