# -*- coding: utf-8 -*-

q = int(input())
v = list(map(int, input().split()))

s = 0

for i in v:

    if i == 0:

        s += 1

if s > len(v) / 2:

    print("Y")
else:

    print("N")