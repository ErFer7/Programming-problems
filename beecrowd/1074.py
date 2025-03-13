# -*- coding: utf-8 -*-

numberOfCases = int(input())

numbers = [None] * numberOfCases

for i in range(numberOfCases):

    numbers[i] = int(input())

for i in numbers:

    result = ""

    if i != 0:

        if i % 2 == 0:

            result = "EVEN"
        else:

            result = "ODD"
        
        if i > 0:

            result += " POSITIVE"
        else:

            result += " NEGATIVE"
    else:

        result = "NULL"

    print(result)