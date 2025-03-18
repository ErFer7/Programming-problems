# -*- coding: utf-8 -*-

from math import fabs

n = int(input())

for i in range(n):

    xy = list(map(float, input().split()))

    area = fabs((xy[0] * (xy[3] - xy[5]) + xy[2] * (xy[5] - xy[1]) + xy[4] * (xy[1] - xy[3])) / 2) 

    print("{:.3f}".format(area))