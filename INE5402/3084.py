# -*- coding: utf-8 -*-

while True:

    try:
        
        hm = list(map(float, input().split()))

        h = int((hm[0] / 360) * 12)
        m = int((hm[1] / 360) * 60)

        if m == 60:
            m = 0

        print("{:02d}:{:02d}".format(h, m))
    except (EOFError, IndexError):
        break