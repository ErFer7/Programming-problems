# -*- coding: utf-8 -*-

n = int(input())

for _ in range(n):

    ls = ""

    s = input()

    for c in s:

        if c.islower():

            ls += c

    print(ls[::-1])