# -*- coding: utf-8 -*-

from math import sqrt

nStr = input().split()
nMap = map(int, nStr)
nLst = list(nMap)

if sqrt(nLst[0]**2 + nLst[1]**2 + nLst[2]**2) / 2 <= nLst[3]:

    print("S")
else:

    print("N")