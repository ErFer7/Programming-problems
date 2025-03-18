# -*- coding: utf-8 -*-

counter = 0

while True:

    rectList = []

    xList = []
    yList = []
    uList = []
    vList = []

    counter += 1

    n = int(input())

    if n == 0:
        break

    for i in range(n):

        rect = list(map(int, input().split()))
        rectList.append(rect)

        xList.append(rect[0])
        yList.append(rect[1])
        uList.append(rect[2])
        vList.append(rect[3])

    xInter = max(xList)
    yInter = min(yList)
    uInter = min(uList)
    vInter = max(vList)

    print("Teste {0}".format(counter))

    if xInter < uInter and yInter > vInter:

        print("{0} {1} {2} {3}\n".format(xInter, yInter, uInter, vInter))
    else:
        
        print("nenhum\n")