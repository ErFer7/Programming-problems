# -*- coding: utf-8 -*-

count = 0

while True:

    count += 1

    a, v = map(int, input().split())

    aList = [0] * a

    if a == 0 and v == 0:
        break

    for _ in range(v):

        x, y = map(int, input().split())

        aList[x - 1] += 1
        aList[y - 1] += 1

    print("Teste {0}".format(count))

    mA = []

    for i in range(a):

        if aList[i] == max(aList):

            mA.append(i + 1)
        
    print("{0} \n".format(" ".join(list(map(str, mA)))))