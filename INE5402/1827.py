# -*- coding: utf-8 -*-

while True:

    try:

        n = int(input())
    except EOFError:
        break

    for i in range(n):

        for j in range(n):

            num = 0

            if i == j and (i < n // 3 or i > n - n // 3 - 1):

                num = 2
            elif i == n - j - 1 and (i < n // 3 or i > n - n // 3 - 1):

                num = 3
            elif i == n // 2 and i == j:

                num = 4
            elif i >= n // 3 and j >= n // 3 and i <= n - n // 3 - 1 and j <= n - n // 3 - 1:

                num = 1

            print(num, end = "")

        print("")
    
    print("")