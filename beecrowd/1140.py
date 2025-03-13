# -*- coding: utf-8 -*-

while True:

    s = input().split()
    c = s[0][0].lower()

    if c == "*":
        break

    t = True

    for w in s:

        if w[0].lower() != c:

            t = False

    if t:

        print("Y")
    else:

        print("N")