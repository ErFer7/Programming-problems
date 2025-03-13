# -*- coding: utf-8 -*-

nCases = int(input())

for i in range(nCases):

    nT = int(input())
    nStr = input().split()
    nMap = map(int, nStr)
    nLst = list(nMap)
    nB = int(input())

    dLst = nLst[:]
    dLst.append(nT)
    dLst.append(nB)

    lst = [1, 2, 3, 4, 5, 6]
    dLst.sort()

    if nT + nB == 7 and nLst[0] + nLst[2] == 7 and nLst[1] + nLst[3] == 7 and dLst == lst:

        print("SIM")
    else:

        print("NAO")