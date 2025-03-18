# -*- coding: utf-8 -*-

while True:

    try:

        s = input()

        t = str.maketrans("1234567890-=WERTYUIOP[]\SDFGHJKL;'XCVBNM,./", "`1234567890-QWERTYUIOP[]ASDFGHJKL;ZXCVBNM,.")

        print(s.translate(t))

    except EOFError:
        break