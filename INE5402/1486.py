# -*- coding: utf-8 -*-

while True:

    pY = []
    c = []
    cI = 0
    pC = 0
    l = 0

    pnc = list(map(int, input().split()))

    if pnc[0] == 0 and pnc[1] == 0 and pnc[2] == 0:
        break

    for i in range(pnc[1]):
        
        pX = list(map(int, input().split()))
        pY.append(pX)
    
    for i in range(pnc[0]):

        for i in pY:

            c.append(i[cI])
        
        for i in range(len(c)):

            if c[i] == 1:

                l += 1
            
            if c[i] == 0 or i == len(c) - 1:

                if l >= pnc[2]:

                    pC += 1
                
                l = 0

        c.clear()
        cI += 1
    
    print(pC)