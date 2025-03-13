# -*- coding: utf-8 -*-

nStr = input().split()
nMap = map(int, nStr)
nLst = list(nMap)

if nLst[0] * nLst[2] <= nLst[1]:

    print("S")
else:

    print("N")