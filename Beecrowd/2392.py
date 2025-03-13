# -*- coding: utf-8 -*-

'''
Pulo do Sapo
'''

stones, frogs = map(int, input().split())

river = [0] * stones

for _ in range(frogs):

    initial_position, jump_distance = map(int, input().split())

    river[initial_position - 1] = 1

    nDistance = 0

    while True:

        nDistance += 1

        if initial_position + jump_distance * nDistance - 1 < stones:
            river[initial_position + jump_distance * nDistance - 1] = 1
        else:

            nDistance = 0
            break

    while True:

        nDistance += 1

        if initial_position - jump_distance * nDistance - 1 >= 0:
            river[initial_position - jump_distance * nDistance - 1] = 1
        else:
            break

for i in river:

    print(i)
