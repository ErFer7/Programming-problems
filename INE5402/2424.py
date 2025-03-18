# -*- coding: utf-8 -*-

'''
Tira-teima
'''

x, y = map(int, input().split())

if  0 <= x <= 432:

    if 0 <= y <= 468:
        print("dentro")
    else:
        print("fora")
else:
    print("fora")
