# -*- coding: utf-8 -*-

from math import ceil

while True:

    n = int(input())

    if n == 0:
        break

    for i in range(n):

        for j in range(n):

            res = ceil((n - abs(i - j) - abs(j + i - (n - 1))) / 2)

            spc = ""

            if j == 0 or res > 9:

                spc = "  "
            elif j <= n - 1:

                spc = "   "

            print("{0}{1}".format(spc, res), end = "")
        
        print("")
    
    print("")