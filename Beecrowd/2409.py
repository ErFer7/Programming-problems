# -*- coding: utf-8 -*-

dCStr = input().split()
dCMap = map(int, dCStr)
dCLst = list(dCMap)

dPStr = input().split()
dPMap = map(int, dPStr)
dPLst = list(dPMap)

if dCLst[0] <= dPLst[1] and dCLst[1] <= dPLst[0]:

    print("S")
elif dCLst[1] <= dPLst[1] and dCLst[0] <= dPLst[0]:

    print("S")
elif dCLst[2] <= dPLst[1] and dCLst[0] <= dPLst[0]:

    print("S")
elif dCLst[0] <= dPLst[1] and dCLst[2] <= dPLst[0]:

    print("S")
elif dCLst[1] <= dPLst[1] and dCLst[2] <= dPLst[0]:

    print("S")
elif dCLst[2] <= dPLst[1] and dCLst[1] <= dPLst[0]:

    print("S")
else:

    print("N")