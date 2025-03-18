# -*- coding: utf-8 -*-

'''
A ideia aqui é criar um dicionário em que cada runa é uma chave com os valores de amizade correspondentes.
Depois disso é feito o somatório com os valores das runas que aparecem, isso é feito usando os valores
correspondentes no dicionário.
'''

n, g = map(int, input().split()) # Entrada de n e g

ru = {} # Dicionário que armazena as runas

for _ in range(n): # Loop para a leitura das runas

    ln = input().split() # Entrada da linha

    ru[ln[0]] = int(ln[1]) # Define a runa como chave e define o valor

x = input() # Entrada da quantidade de runas recitadas (não usado)
lnr = input().split() # Entrada a linha das runas recitadas

a = 0 # Variável para a amizade

for r in lnr: # Para cada runa recitada

    a += ru[r] # Soma o valor correspondente da runa na variável da amizade

print(a) # Exibe a amizade

# Exibe o resultado final
if a >= g:

    print("You shall pass!")
else:

    print("My precioooous")