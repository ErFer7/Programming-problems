# -*- coding: utf-8 -*-

'''
Neste problema foi usada uma lógica simples em que cada palavra do texto é colocado em uma lista. Depois disso é
executado o loop que itera por estas palavras. Se a palavra é igual a palavra procurada então a posição é
adicionada em uma lista. A posição é calculada somando o comprimento de cada palavra e mais "1" para contabilizar
os espaços.

Caso a lista de posições esteja vazias é adicionado "-1". Significando que a palavra não está no texto.
'''

n = int(input()) # Entrada de n

for _ in range(n): # Loop para cada caso

    txt = input().split() # Entrada do texto
    w = input() # Entrada da palavra a ser procurada

    p = 0 # Variável para a posição
    v = [] # Lista para as posições das palavras

    for t in txt: # Para cada palavra no texto

        if t == w: # Caso a palavra seja igual a procurada

            v.append(p) # Adiciona a posição na lista

        p += len(t) + 1 # Calcula a posição
    
    if len(v) == 0: # Caso a palavra não esteja no texto é adicionado "-1" na lista

        v.append(-1)

    print(*v, sep = ' ') # Exibe o resultado