# -*- coding: utf-8 -*-

while True:

    epr = 0
    ehd = 0
    intr = 0

    try:

        n = int(input())
    except EOFError:
        break

    for _ in range(n):

        a = input().split()

        if a[1] == "EPR":

            epr += 1
        elif a[1] == "EHD":

            ehd += 1
        else:

            intr += 1
    
    print("EPR: {0}".format(epr))
    print("EHD: {0}".format(ehd))
    print("INTRUSOS: {0}".format(intr))