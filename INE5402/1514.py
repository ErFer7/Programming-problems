# -*- coding: utf-8 -*-

while True:

    res = 0
    cond = [True, False, True, True]
    mat = []

    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    solv = [0] * m

    for _ in range(n):

        mat.append(list(map(int, input().split())))

    for line in mat:

        if line.count(1) == m:

            cond[0] = False
        
        if line.count(1) == 0:

            cond[3] = False
        
        for i in range(m):

            if solv[i] == 0 and line[i] == 1:

                solv[i] = 1

    checkList = []

    for i in range(m):

        for j in range(n):

            checkList.append(mat[j][i])
        
        if checkList.count(1) == n:

            cond[2] = False
        
        checkList.clear()

    if solv.count(1) == m:

        cond[1] = True

    for c in cond:

        if c:

            res += 1

    print(res)