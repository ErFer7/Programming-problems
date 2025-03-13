# -*- coding: utf-8 -*-

nStr = input().split()
nMap = map(int, nStr)
nLst = list(nMap)

C, F = (0, 0)

C += nLst[0] * 3
C += nLst[1]

F += nLst[3] * 3
F += nLst[4]

if C > F:

    print("C")
elif F > C:

    print("F")
else:

    if nLst[2] > nLst[5]:

        print("C")
    elif nLst[5] > nLst[2]:

        print("F")
    else:

        print("=")