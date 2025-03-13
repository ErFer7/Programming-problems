# -*- coding: utf-8 -*-

cod = ["GQaku", "ISblv", "EOYcmw", "FPZdnx", "JTeoy", "DNXfpz", "AKUgq", "CMWhr", "BLVis", "HRjt"]

n = int(input())

for _ in range(n):

    pw = input().strip(" ")[:20]
    res = ""

    for c in pw:

        for i in range(len(cod)):

            if c in cod[i]:

                res += str(i)
                break
    
    print(res[:12])