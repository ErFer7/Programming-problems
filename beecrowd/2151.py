# -*- coding: utf-8 -*-

c = int(input())

for i in range(c):

    wMat = []

    m, n, x, y = map(int, input().split())

    x -= 1
    y -= 1

    for _ in range(m):

        wMat.append(list(map(int, input().split())))

    for j in range(m):

        for k in range(n):
            
            dist = max(abs(j - x), abs(k - y))

            if dist > 8:

                wMat[j][k] += 1
            else:

                wMat[j][k] += 10 - dist

    print("Parede {0}:".format(i + 1))

    for line in wMat:

        print(" ".join(map(str, line)))