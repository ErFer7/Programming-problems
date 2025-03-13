# -*- coding: utf-8 -*-

# Idade de Mônica, do filho 1 e filho 2
m = int(input())
a = int(input())
b = int(input())

# Idade do filho 3 que deve ser calculada
c = m - (a + b)

# A lógica abaixo compara se cada idade é maior que as outras duas,
# ou seja caso ela seja idade do filho mais velho

# Compara se a é a maior idade
if a > b and a > c:

    print(a)
# Compara se b é a maior idade
elif b > a and b > c:

    print(b)
# Compara se c é a maior idade
elif c > a and c > b:

    print(c)