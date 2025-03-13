# -*- coding: utf-8 -*-

while True:

    try:

        n = int(input())
    except EOFError:
        break

    cod = []

    for _ in range(n):

        cod.append(int(input()))
    
    cod.sort()

    for c in cod:

        res = ""

        if c <= 9:

            res = "000" + str(c)
        elif c <= 99:

            res = "00" + str(c)
        elif c <= 999:

            res = '0' + str(c)
        else:

            res = str(c)
        
        print(res)