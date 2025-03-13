# -*- coding: utf-8 -*-

test = 0

while True:

    test += 1

    deposits = int(input())

    if deposits == 0:
        break

    delta = 0

    print("Teste %d" % test)

    for i in range(deposits):

        values = input().split()

        a = int(values[0])
        b = int(values[1])

        delta += a - b

        print(delta)

    print("")