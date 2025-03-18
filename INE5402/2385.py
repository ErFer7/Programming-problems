# -*- coding: utf-8 -*-

n = int(input())
p, q, r, s, x, y = map(int, input().split())
i, j = map(int, input().split())

res = 0

for k in range(1, n + 1):

    res += ((p * i + q * k) % x) * ((r * k + s * j) % y)
    
print(res)