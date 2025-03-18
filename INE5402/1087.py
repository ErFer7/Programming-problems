# -*- coding: utf-8 -*-

cases = [None]

while True:

    pointsInput = input()
    points = pointsInput.split()

    if points[0] == "0":

        break
    else:

        if (cases[0] == None):

            cases[0] = points
        else:

            cases.append(points)

for i in cases:
    
    x1 = int(i[0])
    y1 = int(i[1])
    x2 = int(i[2])
    y2 = int(i[3])

    if x1 == x2 and y1 == y2:

        print(0)
    elif (x1 == x2 or y1 == y2) or (abs(x2 - x1) == abs(y2 - y1)):

        print(1)
    else:

        print(2)