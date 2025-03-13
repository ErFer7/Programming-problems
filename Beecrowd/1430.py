# -*- coding: utf-8 -*-

n = {'W': 1.0, 'H': 0.5, 'Q': 0.25, 'E': 0.125, 'S': 0.0625, 'T': 0.03125, 'X': 0.015625}

while True:

    cn = 0
    ln = input().split('/')

    if ln[0] == '*':
        break

    for comp in ln:

        t = 0

        for char in comp:

            t += n[char]

        if t == 1.0:

            cn += 1
    
    print(cn)