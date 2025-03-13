# -*- coding: utf-8 -*-

res = 0

n, m = map(int, input().split())

for _ in range(n):

    p = list(map(int, input().split()))

    if 0 not in p:

        res += 1
    
print(res)