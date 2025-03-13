# -*- coding: utf-8 -*-

# Código do professor

while True:

    l, c, p = map(int, input().split())
    p -= 1
    
    if l == 0 and c == 0:
        break
        
    bL = -1
    bC = -1

    for i in range(l):
        
        cols = input().split()
        
        if bL != -1:
            continue
            
        for j in range(c):
            cols[j] = int(cols[j])
            
        if cols[p] != 0:

            bL = i
            bC = p
            continue
            
        jE = 0

        for j in range(p, -1, -1):

            if cols[j] > 0:

                jE = j
                break
                
        jD = c - 1
        for j in range(p, c):

            if cols[j] > 0:
                
                jD = j
                break
                
        des = cols[jE] - cols[jD]
            
        nP = p + des

        if nP < 0:

            nP = 0
        if nP >= c:

            nP = c - 1

        if nP > p:

            while p <= nP:

                if cols[p] != 0:

                    bL = i
                    bC = p
                    break

                p+=1
        elif nP < p:

            while p >= nP:

                if cols[p] != 0:

                    bL = i
                    bC = p
                    break

                p-=1

        p = nP

        
    if bL != -1:
        print("BOOM %d %d" % (bL + 1, bC + 1))
    else:
        print("OUT %d" % (p + 1))