# -*- coding: utf-8 -*-

n = int(input())

for i in range(1, n + 1):

    if i % 2 == 0:

        print("%d^2 = %d" % (i, i**2))