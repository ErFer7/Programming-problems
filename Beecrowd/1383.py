# -*- coding: utf-8 -*-

n = int(input())

for i in range(n):

    valid = True
    mat = []
    numCheck = []

    for _ in range(9):

        line = list(map(int, input().split()))

        for num in line:

            if num not in numCheck and num >= 1 and num <= 9:

                numCheck.append(num)
        
        if valid:

            if len(numCheck) != 9:

                valid = False
            else:

                mat.append(line)
            
        numCheck.clear()
    
    print("Instancia {0}".format(i + 1))

    if valid:

        for j in range(9):

            for k in range(9):

                if mat[k][j] not in numCheck and mat[k][j] >= 1 and mat[k][j] <= 9:

                    numCheck.append(mat[k][j])

            if len(numCheck) != 9:

                valid = False
                break

            numCheck.clear()

    if valid:
        
        for j in range(0, 7, 3):

            if valid:

                for k in range(0, 7, 3):

                    for l in range(j, j + 3):

                        for m in range(k, k + 3):

                            if mat[l][m] not in numCheck and mat[l][m] >= 1 and mat[l][m] <= 9:

                                numCheck.append(mat[l][m])

                    if len(numCheck) != 9:

                        valid = False
                        break

                    numCheck.clear()
            else:
                
                break

    if valid:

        print("SIM\n")
    else:

        print("NAO\n")