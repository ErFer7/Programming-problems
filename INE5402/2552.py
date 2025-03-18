# -*- coding: utf-8 -*-

while True:

    try:

        n, m = map(int, input().split())
    except EOFError:
        break

    mat = []
    resMat = []
    for _ in range(n):

        mat.append(list(map(int, input().split())))

    for i in range(n):

        resMat.append([])
        for j in range(m):

            resMat[i].append(0)

            if mat[i][j] == 1:

                resMat[i][j] = 9
            else:

                if i > 0 and mat[i - 1][j] == 1:

                    resMat[i][j] += 1
                
                if i < n - 1 and mat[i + 1][j] == 1:

                    resMat[i][j] += 1

                if j > 0 and mat[i][j - 1] == 1:

                    resMat[i][j] += 1
                
                if j < m - 1 and mat[i][j + 1] == 1:

                    resMat[i][j] += 1
        
        print("".join(map(str, resMat[i])))