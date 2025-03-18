# -*- coding: utf-8 -*-

finished = False
mat = []
walkedPos = []

l, c = map(int, input().split())
a, b = map(int, input().split())

for _ in range(l):

    mat.append(list(map(int, input().split())))

while not finished:

    walkedPos.append([a - 1, b - 1])

    if a > 1 and mat[a - 2][b - 1] == 1 and [a - 2, b - 1] not in walkedPos:

        a -= 1
    elif a < l and mat[a][b - 1] == 1 and [a, b - 1] not in walkedPos:

        a += 1
    elif b > 1 and mat[a - 1][b - 2] == 1 and [a - 1, b - 2] not in walkedPos:

        b -= 1
    elif b < c and mat[a - 1][b] == 1 and [a - 1, b] not in walkedPos:

        b += 1
    else:

        finished = True

print("{0} {1}".format(a, b))