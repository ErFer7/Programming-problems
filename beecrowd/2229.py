# -*- coding: utf-8 -*-

test = 0

while True:

    test += 1

    D = int(input())

    if D == -1:
        break

    print("Teste %d" % test)
    print((2 ** D - 1) ** 2 + 4 * (2 ** D - 1) + 4)
    print("")