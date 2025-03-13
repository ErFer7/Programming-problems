# -*- coding: utf-8 -*-

n = int(input())
result = 0

for i in range(n):

    lc = input().split()

    l = int(lc[0])
    c = int(lc[1])

    if l > c:

        result += c

print(result)