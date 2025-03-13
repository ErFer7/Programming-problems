# -*- coding: utf-8 -*-

'''
Distância Entre Dois Pontos
'''

from math import sqrt

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"{distance:.4f}")
