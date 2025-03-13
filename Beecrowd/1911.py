# -*- coding: utf-8 -*-

while True:

    d = {}
    count = 0

    n = int(input())

    if n == 0:
        break

    for _ in range(n):

        ln = input().split()

        d[ln[0]] = ln[1]

    m = int(input())

    for _ in range(m):

        ln = input().split()

        e = 0

        for i in range(len(ln[1])):

            if ln[1][i] != d[ln[0]][i]:

                e += 1

        if e > 1:

            count += 1

    print(count)