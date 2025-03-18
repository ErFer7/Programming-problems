# -*- coding: utf-8 -*-

# A ideia é comparar a soma de cada valor usando dois loops. O primeiro loop representa cada valor na lista e o
# segundo loop é usado para comparar esse valor com cada valor que vem em sequência na lista.

# Variável para o resultado
res = 0

# Input do número de elementos na lista, valor mínimo e máximo respectivamente
n, i, f = map(int, input().split())

# Input da lista
v = list(map(int, input().split()))

# Loop para cada valor na lista
for j in range(n):

    # Loop de comparação com cada valor subsequente na lista a partir do valor "j"
    for k in range(j, n):

        # Compara se o número não é ele mesmo e faz os somatórios e compara se (j + k >= i e j + k <= f) são verdadeiros
        if j != k and v[j] + v[k] >= i and v[j] + v[k] <= f:

            # Incrementa o resultado
            res += 1

# Exibe o resultado
print(res)