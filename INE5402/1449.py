# -*- coding: utf-8 -*-

t = int(input())

for _ in range(t):

    d = {}

    m, n = map(int, input().split())

    for _ in range(m):

        w = input()
        d[w] = input()
    
    for _ in range(n):

        ly = input().split()
        ln = ''

        for i in range(len(ly)):

            if ly[i] in d.keys():

                if i != 0:

                    ln += ' ' + d[ly[i]]
                else:

                    ln += d[ly[i]]
            else:

                if i != 0:

                    ln += ' ' + ly[i]
                else:

                    ln += ly[i]
        
        print(ln)
    
    print('')