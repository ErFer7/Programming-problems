# -*- coding: utf-8 -*-

while True:

    d = {}
    func = True
    inv = True

    t = int(input())

    if t == 0:
        break

    for _ in range(t):

        ln = input().split()

        if ln[0] not in d.keys():
            
            d[ln[0]] = ln[2]
        else:

            func = False
    
    if func:

        for v in d.values():

            if list(d.values()).count(v) > 1:

                inv = False
                print("Not invertible.")
                break
        
        if inv:

            print("Invertible.")
    else:

        print("Not a function.")