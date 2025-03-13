# -*- coding: utf-8 -*-

'''
Código do professor (um pouco modificado)
'''

n, k = map(int, input().split())

qD = [None] * n

for i in range(n):

    qD[i] = [0] * n
    
for x in range(k):

    i, j, d = map(int, input().split())

    for a in range(n):

        for b in range(n):

            if abs(a - i) + abs(b - j) == d:

                qD[a][b] += 1

iT = -1
jT = -1
q = 0

for i in range(n):

    for j in range(n):

        if qD[i][j] == k:

            iT = i
            jT = j
            q += 1

            if q > 1:

                break
    if q > 1:

        break

if q > 1:

    print("-1 -1")
else:

    print("{0} {1}".format(iT, jT))
