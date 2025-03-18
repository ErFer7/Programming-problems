# -*- coding: utf-8 -*-

while True:

    try:

        n, m = map(int, input().split())
    except EOFError:

        break

    mat = []

    lI, cI = 0, 0
    lF, cF = 0, 0

    for i in range(n):

        line = list(map(int, input().split()))

        if 1 in line:

            lI = i
            cI = line.index(1)
    
        if 2 in line:

            lF = i
            cF = line.index(2)

        mat.append(line)
    
    print(abs(lF - lI) + abs(cF - cI))