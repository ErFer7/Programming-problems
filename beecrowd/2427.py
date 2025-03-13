# -*- coding: utf-8 -*-

l = int(input())
p = 1
n = 1

while l >= 2:

    l /= 2
    p = 4**n
    n += 1

print(p)