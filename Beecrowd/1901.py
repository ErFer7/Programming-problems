# -*- coding: utf-8 -*-

'''
A ideia aqui é usar uma lista para verificar quais espécies já foram encontradas.

A cada posição que Bino anda é verificado se a espécie é nova ou não, caso seja nova ela é adicionada na lista.
No fim o comprimento da lista será a quantidade de espécies encontradas.
'''

n = int(input()) # Entrada de n

mat = [] # Matriz que representa a floresta

# Loop para a entrada da matriz
for _ in range(n):

    mat.append(list(map(int, input().split())))

e = [] # Lista de espécies

for _ in range(n * 2): # Para cada posição andada

    i, j = map(int, input().split()) # Obtém as coordenadas

    # Subtrái "1" para tornar os índices válidos na matriz
    i -= 1
    j -= 1

    if mat[i][j] not in e: # Se a espécie não está na lista

        e.append(mat[i][j]) # Adiciona a espécie na lista

print(len(e)) # Exibe o resultado que será o próprio comprimento da lista