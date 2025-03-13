# -*- coding: utf-8 -*-

n = int(input())

count = {'A': 0, 'E': 0, 'H': 0, 'M': 0, 'X': 0}

for _ in range(n):

    ln = input().split()

    count[ln[1]] += 1

print("{0} Hobbit(s)".format(count['X']))
print("{0} Humano(s)".format(count['H']))
print("{0} Elfo(s)".format(count['E']))
print("{0} Anao(s)".format(count['A']))
print("{0} Mago(s)".format(count['M']))