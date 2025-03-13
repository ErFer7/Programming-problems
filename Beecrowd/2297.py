# -*- coding: utf-8 -*-

counter = 0

while True:

    a = 0
    b = 0

    counter += 1

    r = int(input())

    if r == 0:
        break

    for i in range(r):

        ab = list(map(int, input().split()))
        a += ab[0]
        b += ab[1]

    print("Teste {0}".format(counter))

    if a > b:

        print("Aldo\n")
    else:

        print("Beto\n")