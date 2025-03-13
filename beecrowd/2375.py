# -*- coding: utf-8 -*-

dB = int(input())
dStr = input().split()
dMap = map(int, dStr)
dLst = list(dMap)

if dLst[0] >= dB and dLst[1] >= dB and dLst[2] >= dB:

    print("S")
else:

    print("N")