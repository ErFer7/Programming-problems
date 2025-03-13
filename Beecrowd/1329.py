# -*- coding: utf-8 -*-

while True:

    nStr = input()
    n = int(nStr)

    if n == 0:
        break

    gamesStr = input().split()
    gamesMap = map(int, gamesStr)
    games = list(gamesMap)

    mary = 0
    john = 0

    for g in games:

        if g == 0:

            mary += 1
        else:

            john += 1
    
    print("Mary won {0} times and John won {1} times".format(mary, john))