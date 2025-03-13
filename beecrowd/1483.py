# -*- coding: utf-8 -*-

g = {}

for i in range(25):

    for j in range(1, 5):

        k = j + 4 * i


        if k != 100:

            g[str(k)] = i
        else:

            g['0'] = i

while True:

    res = 0
    comp = False

    v, n, m = input().split()

    if v == '0' and n == '0' and m == '0':
        break

    v = float(v)

    if int(n[-4:]) == int(m[-4:]):

        res = v * 3000.0
        comp = True
    elif not comp and int(n[-3:]) == int(m[-3:]):

        res = v * 500.0
        comp = True
    elif not comp and int(n[-2:]) == int(m[-2:]):

        res = v * 50.0
        comp = True
    elif not comp and g[str(int(n[-2:]))] == g[str(int(m[-2:]))]:

        res = v * 16.0
        comp = True
    
    print("{0:.2f}".format(res))