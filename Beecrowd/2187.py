# -*- coding: utf-8 -*-

'''
Bits Trocados
'''

test = 0

while True:

    test += 1

    value = int(input())

    if value == 0:
        break

    notes_50 = value // 50
    value -= 50 * notes_50

    notes_10 = value // 10
    value -= 10 * notes_10

    notes_5 = value // 5
    value -= 5 * notes_5

    notes_1 = value

    print(f"Teste {test}")
    print(f"{notes_50} {notes_10} {notes_5} {notes_1}\n")
