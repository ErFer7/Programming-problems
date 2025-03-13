# -*- coding: utf-8 -*-

# Código do professor

mat = [None] * 100
    
while True:

    try:

        m, n = map(int, input().split())
    except EOFError:
        break
        
    y, x = 0, 0
    for i in range(m):

        mat[i] = input().split()
        
        for j in range(n):
            
            if mat[i][j] == 'X':

                y, x = i, j
                    
    lastDir = 'B'

    while True:

        move = ''
            
        if x > 0 and mat[y][x - 1] == '0':

            x = x - 1

            if lastDir == 'C': 

                move = 'L' 
            elif lastDir == 'B':

                move = 'R'
            else:

                move = 'F'

            lastDir = 'E'
                
        if move == '' and x < n - 1 and mat[y][x + 1] == '0':

            x = x + 1

            if lastDir == 'C':

                move = 'R'
            elif lastDir == 'B':

                move = 'L'
            else:

                move = 'F'

            lastDir = 'D'
                    
        if move == '' and y > 0 and mat[y - 1][x] == '0':

            y = y - 1
            if lastDir == 'E':

                move = 'R'
            elif lastDir == 'D':

                move = 'L'
            else:

                move = 'F'
            lastDir = 'C'

        if move == '' and y < m - 1 and mat[y+1][x] == '0':

            y = y + 1
            if lastDir == 'E':

                move = 'L'
            elif lastDir == 'D':

                move = 'R'
            else:

                move = 'F'

            lastDir = 'B'
        
        if move == '':

            print('E')
            break
                
        mat[y][x] = '1'

        if move != 'F':

            print(move + ' F', end = ' ')
        else:

            print(move, end = ' ')