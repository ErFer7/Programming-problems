# -*- coding: utf-8 -*-

n = int(input())

for _ in range(n):

    d = {}
    c = 0.0

    m = int(input())

    for _ in range(m):

        ln = input().split()

        d[ln[0]] = float(ln[1])
    
    o = int(input())

    for _ in range(o):

        ln = input().split()

        c += d[ln[0]] * float(ln[1])
    
    print("R$ {0:.2f}".format(c))