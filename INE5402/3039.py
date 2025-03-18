# -*- coding: utf-8 -*-

# Para este problema basta verificar qual é o caractere que vem ao lado de cada nome e incrementar as respectivas
# variáveis para a quantidade de carrinhos (quando o caractere é M) e bonecas (quando o caractere é F).

# Variáveis para carrinhos (c) e bonecas (b)
c, b = 0, 0

# Input do número de crianças
n = int(input())

# Loop que itera sobre as entradas
for _ in range(n):

    # Caso o segundo string da lista é M
    if input().split()[1] == "M":

        # Incrementa a quantidade de carrinhos
        c += 1
    # Caso contrário o caractere será F, ou seja a criança é menina
    else:

        # Incrementa a quantidade de bonecas
        b += 1

# Exibe na tela o resultado
print("{0} carrinhos\n{1} bonecas".format(c, b))