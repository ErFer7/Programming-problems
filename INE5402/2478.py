# -*- coding: utf-8 -*-

'''
A ideia aqui é usar um dicionário para armazenar os presentes. Cada nome é uma chave e os presentes ficam em um
vetor naquela chave. Quando é feita uma consulta ao programa é verificado se o presente está no vetor daquela
chave (nome) e se o nome fornecido está no dicionário. Depois disso é exibido o resultado.
'''

x = int(input()) # Entrada de x

d = {} # Dicionário para os presentes

for _ in range(x): # Loop para cada nome

    ln = input().split() # Entrada da linha

    # Coloca o nome no dicionário como uma chave e coloca os presentes em um vetor nesta chave
    d[ln[0]] = (ln[1], ln[2], ln[3])

while True: # Loop para cada consulta

    # No caso do fim do arquivo quebra o loop
    try:

        ln = input().split() # Entrada da linha
    except EOFError:
        break
    
    # Caso o presente esteja na lista de presentes desejados e está também no dicionário
    if ln[0] in d.keys() and ln[1] in d[ln[0]]:

        print("Uhul! Seu amigo secreto vai adorar o/") # Exibe o resultado
    else: # Caso contrário

        print("Tente Novamente!") # Exibe o resultado