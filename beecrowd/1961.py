# -*- coding: utf-8 -*-

import math

p, n = map(int, input().split())
c = list(map(int, input().split()))

v = True

for i in range(n - 1):

    if abs(c[i + 1] - c[i]) > p:

        v = False

if v:

    print("YOU WIN")
else:

    print("GAME OVER")