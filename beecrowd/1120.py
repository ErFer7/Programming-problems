# -*- coding: utf-8 -*-

while True:

    d, n = map(str, input().split())

    if d == "0" and n == "0":
        break

    vStr = n.replace(d, "")

    if vStr == "":

        vStr = "0"
    
    print(int(vStr))