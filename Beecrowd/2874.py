# -*- coding: utf-8 -*-

while True:

    try:

        n = int(input())
        res = ""

        for _ in range(n):

            res += bytes([int(input(), 2)]).decode("cp437")

        print(res)
    except EOFError:
        break