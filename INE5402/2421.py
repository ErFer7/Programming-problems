# -*- coding: utf-8 -*-

xy = list(map(int, input().split()))
lh0 = list(map(int, input().split()))
lh1 = list(map(int, input().split()))

if lh0[1] + lh1[1] <= xy[1] and max(lh0[0], lh1[0]) <= xy[0]:

    print("S")
elif lh0[0] + lh1[1] <= xy[1] and max(lh0[1], lh1[0]) <= xy[0]:

    print("S")
elif lh0[1] + lh1[0] <= xy[1] and max(lh0[0], lh1[1]) <= xy[0]:

    print("S")
elif lh0[0] + lh1[0] <= xy[1] and max(lh0[1], lh1[1]) <= xy[0]:

    print("S")
elif lh0[0] + lh1[0] <= xy[0] and max(lh0[1], lh1[1]) <= xy[1]:

    print("S")
elif lh0[0] + lh1[1] <= xy[0] and max(lh0[1], lh1[0]) <= xy[1]:

    print("S")
elif lh0[1] + lh1[0] <= xy[0] and max(lh0[0], lh1[1]) <= xy[1]:

    print("S")
elif lh0[1] + lh1[1] <= xy[0] and max(lh0[0], lh1[0]) <= xy[1]:

    print("S")
else:

    print("N")