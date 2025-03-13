# -*- coding: utf-8 -*-

d = {}

n = int(input())

for _ in range(n):

    lang = input()
    d[lang] = input()

m = int(input())

for _ in range(m):

    print(input())
    print(d[input()])
    print('')