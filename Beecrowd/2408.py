# -*- coding: utf-8 -*-

nStr = input().split()
nMap = map(int, nStr)
nLst = list(nMap)

for i in nLst:

    if i > min(nLst) and i < max(nLst):

        print(i)