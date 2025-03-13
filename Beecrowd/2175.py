# -*- coding: utf-8 -*-

obi = list(map(float, input().split()))

a = obi.index(min(obi))

obi_s = set(obi)

if len(obi_s) == len(obi):

    if a == 0:

        print("Otavio")
    elif a == 1:

        print("Bruno")
    else:

        print("Ian")
else:

    print("Empate")