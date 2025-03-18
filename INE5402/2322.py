# -*- coding: utf-8 -*-

# Este programa usa um loop que itera por todos os valores de 1 a N e checa se o valor não está na lista de números,
# caso o valor não esteja ele é exibido.

# Input do N
n = int(input())

# Input da lista de números que representam as peças
v = list(map(int, input().split()))

# Loop para os valores a serem checados (1 a N)
for i in range(1, n + 1):

    # Caso a lista não contenha o valor i
    if i not in v:

        # Exibe o valor i
        print(i)