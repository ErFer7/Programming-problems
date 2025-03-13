# -*- coding: utf-8 -*-

while True:

    n = int(input())
    result = 0

    if n == 0:

        break

    for i in range(n):

        result += (n - i)**2
    
    print(result)