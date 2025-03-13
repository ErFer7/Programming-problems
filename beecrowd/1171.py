# -*- coding: utf-8 -*-

n = int(input())

d = {}

for _ in range(n):

    num = input()

    if num not in d.keys():

        d[num] = 1
    else:

        d[num] += 1

itens = sorted(list(d.items()), key = lambda x: int(x[0]))

for it in itens:

    print("{0} aparece {1} vez(es)".format(it[0], it[1]))