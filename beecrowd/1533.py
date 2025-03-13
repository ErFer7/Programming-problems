# -*- coding: utf-8 -*-

while True:

    n = int(input())

    if n == 0:
        break

    s = list(map(int, input().split()))

    a = s[:]
    a.sort()
    print(s.index(a[-2]) + 1)