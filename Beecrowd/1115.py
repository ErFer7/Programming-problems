# -*- coding: utf-8 -*-

while True:
    
    xy = list(map(int, input().split()))

    if xy[0] == 0 or xy[1] == 0:
        break

    if xy[0] > 0:

        if xy[1] > 0:

            print("primeiro")
        else:

            print("quarto")
    else:

        if xy[1] > 0:

            print("segundo")
        else:

            print("terceiro")