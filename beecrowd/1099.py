# -*- coding: utf-8 -*-

totalCases = int(input())
cases = [None]

for i in range(totalCases):

    numbers = input().split()

    if cases[0] == None:

        cases[0] = numbers
    else:

        cases.append(numbers)

for i in cases:

    n0 = int(i[0])
    n1 = int(i[1])

    if n0 > n1:

        temp = n0
        n0 = n1
        n1 = temp

    result = 0

    for j in range(n0 + 1, n1):

        if j % 2 != 0:

            result += j
        
    print(result)