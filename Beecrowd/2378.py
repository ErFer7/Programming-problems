# -*- coding: utf-8 -*-

nc = list(map(int, input().split()))
a = 0
b = "N"

for i in range(nc[0]):

    se = list(map(int, input().split()))

    a += se[1] - se[0]

    if a > nc[1]:

        b = "S"

print(b)