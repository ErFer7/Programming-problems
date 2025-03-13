# -*- coding: utf-8 -*-

''' Ideia: Para resolver o problema basta contar quantos números únicos estão na lista. Sendo assim se o mesmo
número aparecer mais de uma vez ele será contado apenas uma vez. É possível transformar essa lista em um set, já
que set não permite repetição. Com isso basta usar a função len() e obter a quantidade de números do set.
'''

v = []                          # Lista para os números dos alunos

n = int(input())                # Entrada da quantidade de registros

for _ in range(n):              # Loop para registrar cada número

    v.append(int(input()))      # Adiciona o número na lista

print(len(set(v)))              # Exibe na tela o comprimento do set criado a partir da lista