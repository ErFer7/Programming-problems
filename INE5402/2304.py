# -*- coding: utf-8 -*-

i, n = map(int, input().split())

d, e, f = i, i, i

for _ in range(n):

    op = input().split()

    if op[0] == "C":

        if op[1] == "D":

            d -= int(op[2])
        elif op[1] == "E":

            e -= int(op[2])
        else:

            f -= int(op[2])
    elif op[0] == "V":

        if op[1] == "D":

            d += int(op[2])
        elif op[1] == "E":

            e += int(op[2])
        else:

            f += int(op[2])
    else:

        if op[1] == "D":

            d += int(op[3])
        elif op[1] == "E":

            e += int(op[3])
        else:

            f += int(op[3])
        
        if op[2] == "D":

            d -= int(op[3])
        elif op[2] == "E":

            e -= int(op[3])
        else:

            f -= int(op[3])

print("{0} {1} {2}".format(d, e, f))