# -*- coding: utf-8 -*-

import math

numberOfCases = int(input())

for i in range(numberOfCases):

    number = int(input())
    isPrime = True

    if number % 2 == 0 and number > 2:

        isPrime = False
    else:

        root = int(math.sqrt(number))

        for j in range(3, root + 1, 2):

            if number % j == 0:

                isPrime = False
                break
    
    if isPrime:

        print("Prime")
    else:

        print("Not Prime")