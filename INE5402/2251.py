# -*- coding: utf-8 -*-

count = 0

while True:

    count += 1

    n = int(input())

    if n == 0:
        break

    print("Teste {0}".format(count))
    print("{0}".format(2 ** n - 1))
    print()