# -*- coding: utf-8 -*-

a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

horizontalAxisMax = x // a
longitudinalAxisMax = y // b
verticalAxisMax = z // c

print(horizontalAxisMax * longitudinalAxisMax * verticalAxisMax)