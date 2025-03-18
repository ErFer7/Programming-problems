# -*- coding: utf-8 -*-

ns = list(map(int, input().split()))
minS = ns[1]

for i in range(ns[0]):

    ns[1] += int(input())

    if ns[1] < minS:

        minS = ns[1]

print(minS)