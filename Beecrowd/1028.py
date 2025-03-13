# -*- coding: utf-8 -*-

def mdc(a, b):

    if b == 0:

        return a
    else:

        return mdc(b, a % b)

n = int(input())

for _ in range(n):

    r, v = map(int, input().split())

    print(mdc(r, v))