# -*- coding: utf-8 -*-

n = int(input())

t = []

for _ in range(n):

    t.append(int(input()))

for i in range(n):

    if i > 0 and i < n - 1:

        print(sum(t[i - 1:i + 2]))
    elif i == 0:

        print(sum(t[:2]))
    else:

        print(sum(t[i - 1:]))