# -*- coding: utf-8 -*-

hp = {}

m, n = map(int, input().split())

for _ in range(m):

    ln = input().split()

    hp[ln[0]] = int(ln[1])

for _ in range(n):

    s = 0
    
    while True:

        ln = input().split()

        if ln[0] == '.':

            print(s)
            break

        for w in ln:

            try:

                s += hp[w]
            except KeyError:
                continue