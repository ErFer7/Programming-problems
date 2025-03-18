# -*- coding: utf-8 -*-

nStr = input().split()
nMap = map(int, nStr)
nLst = list(nMap)

if nLst[0] + nLst[1] > nLst[2] and nLst[0] + nLst[2] > nLst[1] and nLst[1] + nLst[2] > nLst[0]:

    if nLst[0] != nLst[1] and nLst[0] != nLst[2] and nLst[1] != nLst[2]:

        print("Valido-Escaleno")

    if (nLst[0] == nLst[1] and nLst[0] != nLst[2]) or (nLst[0] == nLst[2] and nLst[0] != nLst[1]) or (nLst[1] == nLst[2] and nLst[1] != nLst[0]):

        print("Valido-Isoceles")
    
    if nLst[0] == nLst[1] and nLst[0] == nLst[2]:

        print("Valido-Equilatero")

    H = max(nLst)
    nLst.remove(H)

    if nLst[0]**2 + nLst[1]**2 == H**2:

        print("Retangulo: S")
    else:

        print("Retangulo: N")
else:

    print("Invalido")