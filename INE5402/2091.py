# -*- coding: utf-8 -*-

while True:

    res = 0
    d = {}

    n = int(input())

    if n == 0:
        break

    v = list(map(int, input().split()))

    for num in v:
 
        if str(num) not in d.keys():

            d[str(num)] = 1
        else:

            d[str(num)] += 1
    
    for k in d:

        if d[k] % 2 != 0:

            res = int(k)
            break

    print(res)