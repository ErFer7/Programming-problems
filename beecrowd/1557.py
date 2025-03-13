# -*- coding: utf-8 -*-

while True:

    n = int(input())

    if n == 0:
        break
    
    spcILen = len(str(4 ** (n - 1)))

    for i in range(n):

        for j in range(n):

            res = 2 ** (i + j)

            spc = ""

            if j == 0:

                spc = " " * (spcILen - len(str(res)))
            elif j <= n - 1:

                spc = " " * (spcILen - len(str(res)) + 1)

            print("{0}{1}".format(spc, res), end = "")
        
        print("")
    
    print("")