# -*- coding: utf-8 -*-

'''
Divisão da Nlogônia
'''

while True:

    input_count = int(input())

    if input_count == 0:
        break

    center_x, center_y = map(int, input().split())

    for _ in range(input_count):

        x, y = map(int, input().split())

        if x == center_x or y == center_y:
            print("divisa")
        else:

            if x > center_x:

                if y > center_y:
                    print("NE")
                else:
                    print("SE")
            else:

                if y > center_y:
                    print("NO")
                else:
                    print("SO")
