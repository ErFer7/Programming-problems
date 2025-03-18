# -*- coding: utf-8 -*-

n = int(input())

c, e, cC, cE = 0, 0, 0, 0

for _ in range(n):

    sd, sn = map(str, input().split())

    if sd == "chuva":

        if c == 0:

            cC += 1
        else:

            c -= 1
        
        e += 1
    
    if sn == "chuva":

        if e == 0:

            cE += 1
        else:

            e -= 1
        
        c += 1

print("{0} {1}".format(cC, cE))