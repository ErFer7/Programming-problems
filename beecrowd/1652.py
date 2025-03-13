# -*- coding: utf-8 -*-

l, n = map(int, input().split())

iW = []
iWP = []

for _ in range(l):

    i = input().split()

    iW.append(i[0])
    iWP.append(i[1])

for _ in range(n):

    w = input()

    if w in iW:

        print(iWP[iW.index(w)])
    elif w.endswith("by") or w.endswith("cy") or w.endswith("dy") or w.endswith("fy") or w.endswith("gy") or \
         w.endswith("hy") or w.endswith("jy") or w.endswith("ky") or w.endswith("ly") or w.endswith("my") or \
         w.endswith("ny") or w.endswith("py") or w.endswith("qy") or w.endswith("ry") or w.endswith("sy") or \
         w.endswith("ty") or w.endswith("vy") or w.endswith("wy") or w.endswith("xy") or w.endswith("zy"):

         print(w[:-1] + "ies")
    elif w.endswith("o") or w.endswith("s") or w.endswith("ch") or w.endswith("sh") or w.endswith("x"):

        print(w + "es")
    else:

        print(w + "s")