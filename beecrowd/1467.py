# -*- coding: utf-8 -*-

while True:

    try:

        case = input().split()
        
        A = int(case[0])
        B = int(case[1])
        C = int(case[2])

        if A == B and A == C:

            print("*")
        elif A == B and A != C:

            print("C")
        elif A != B and A == C:

            print("B")
        elif A != B and A != C:

            print("A")
    except EOFError:
        break