# -*- coding: utf-8 -*-

def iccanobif(n):

    res = [0] * n

    res[n - 1] = 1
    res[n - 2] = 1

    for i in range(n - 3, -1, -1):

        res[i] = res[i + 1] + res[i + 2]
    
    return res

n = int(input())

print(*iccanobif(n), sep = ' ')