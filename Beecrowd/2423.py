# -*- coding: utf-8 -*-

'''
Receita de Bolo
'''

cups, eggs, milk = map(int, input().split())

min_cups = cups // 2
min_eggs = eggs // 3
min_milk = milk // 5

print(min(min_cups, min_eggs, min_milk))
