# -*- coding: utf-8 -*-

def func(pa: list, im: list):

    return sorted(pa) + sorted(im, reverse = True)

n = int(input())

pa = []
im = []

for _ in range(n):

    num = int(input())

    if num % 2 == 0:

        pa.append(num)
    else:

        im.append(num)

res = func(pa, im)

for num in res:

    print(num)