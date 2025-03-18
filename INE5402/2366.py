# -*- coding: utf-8 -*-

nP, iD = map(int, input().split())
dP = list(map(int, input().split()))

f = True

for i in range(nP):

    if i != nP - 1:

        if dP[i + 1] - dP[i] > iD:

            f = False
    else:

        if 42195 - dP[i] > iD:

            f = False

if f:

    print("S")
else:

    print("N")