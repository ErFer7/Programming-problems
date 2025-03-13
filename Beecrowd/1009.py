# -*- coding: utf-8 -*-

'''
Salário com Bônus
'''

name = input()
fixed_salary = float(input())
selled_products = float(input())

print(f"TOTAL = R$ {(fixed_salary + (selled_products * 0.15)):.2f}")
