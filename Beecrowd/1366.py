# -*- coding: utf-8 -*-

while True:

    p = 0

    n = int(input())

    if n == 0:
        break

    for i in range(n):

        cv = list(map(int, input().split()))
        p += cv[1] // 2
    
    print(p // 2)