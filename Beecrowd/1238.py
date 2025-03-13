# -*- coding: utf-8 -*-

n = int(input())

for _ in range(n):

    s1, s2 = map(str, input().split())

    res = ""

    f1 = False
    f2 = False

    i = 0
    while not (f1 and f2):

        if i < len(s1):

            res += s1[i]
            f1 = False
        else:

            f1 = True
        
        if i < len(s2):

            res += s2[i]
            f2 = False
        else:

            f2 = True
        
        i += 1
    
    print(res)