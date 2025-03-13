# -*- coding: utf-8 -*-

n = int(input())

for _ in range(n):

    leds = 0

    v = input()

    for c in v:

        if c == "0" or c == "6" or c == "9":

            leds += 6
        elif c == "1":

            leds += 2
        elif c == "2" or c == "3" or c == "5":
            
            leds += 5
        elif c == "4":

            leds += 4
        elif c == "7":

            leds += 3
        elif c == "8":

            leds += 7
    
    print("{0} leds".format(leds))