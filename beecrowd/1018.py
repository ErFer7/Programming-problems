# -*- coding: utf-8 -*-

'''
Cédulas
'''

value = int(input())

print(value)

bank_notes = [100, 50, 20, 10, 5, 2, 1]

for bank_note in bank_notes:

    print(f"{value // bank_note} nota(s) de R$ {bank_note},00")
    value -= (value // bank_note) * bank_note
