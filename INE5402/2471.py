# -*- coding: utf-8 -*-

# Código do professor

n = int(input())

lnSum = [0] * n
colSum = [0] * n

mat = [None] * n

for i in range(n):

    mat[i] = input().split()

    for j in range(n):

        mat[i][j] = int(mat[i][j])

for i in range(n):

    for j in range(n):

        lnSum[i] += mat[i][j]
        colSum[j] += mat[i][j]

lnSumDif = {}
colSumDif = {}

for i in range(n):

    if not lnSum[i] in lnSumDif:
        
        lnSumDif[lnSum[i]] =  [i]
    else:

        lnSumDif[lnSum[i]].append(i)
        
    if not colSum[i] in colSumDif:

        colSumDif[colSum[i]] = [i]
    else:
        colSumDif[colSum[i]].append(i)

wSum = -1
corSum = -1
wLn = -1

for x in lnSumDif:
    
    if len(lnSumDif[x]) == 1:

        wLn = lnSumDif[x][0]
        wSum = x
    else:
        corSum = x

wCol = -1

for x in colSumDif:

    if len(colSumDif[x]) == 1:

        wCol = colSumDif[x][0]
        break
        
wVal = mat[wLn][wCol]
oVal = wVal + corSum - wSum

print("{0} {1}".format(oVal, wVal))