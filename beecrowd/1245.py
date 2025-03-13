# -*- coding: utf-8 -*-

while True:

    try:

        n = int(input())

        v = [[0 , ""]]
        res = 0

        for _ in range(n):

            b = input().split()

            m = int(b[0])
            l = b[1]

            p = False

            for i in v:

                if i[0] == m and i[1] != l:

                    p = True
                    res += 1
                    v.remove(i)
                    break
            
            if not p:

                v.append([m, l])
                
        print(res)
    except EOFError:
        break