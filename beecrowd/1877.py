# -*- coding: utf-8 -*-

n, k = map(int, input().split())
h = list(map(int, input().split()))

v = 0

for i in range(1, n - 1):

    if h[i] < h[i - 1] and h[i] < h[i + 1]:

        v += 1

if v == k - 1:

    print("beautiful")
else:

    print("ugly")