# -*- coding: utf-8 -*-

def ClearChar(x):

    if x != "[" or x != "]" or x != "'" or x != ",":

        return False
    else:

        return True

while True:

    a = []

    try:

        nr = list(map(int, input().split()))
        b = list(map(int, input().split()))

        a = list(range(1, nr[0] + 1))

        c = list(set(a) ^ set(b))

        if len(c) > 0:

            d = ""
            for i in c:

                d += str(i)
                d += " "

            print(d)
        else:

            print("*")
    except EOFError:
        break