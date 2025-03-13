# -*- coding: utf-8 -*-

'''
Para resolver o problema só é necessário criar um dicionário e armazenar os dígitos nele como chaves.
Quando um dígito não está no dicionário ele é definido como uma chave e recebe o valor 1. Ex: Dígito "2" 
é usado para criar uma chave "2" e coloca o valor 1 nessa chave. Já quando um número está no dicionário ele
é simplesmente somado. Continuando o exemplo com o dígito "2", caso outro "2" seja encontrado o valor nessa
chave é incrementado.

Depois disso é usada a função "max()" para obter a chave com o valor máximo (mais frequente). O parâmetro "key"
de "max()" é usado para especificar como o máximo deve ser obtido. No caso uma função lâmbda é usada para dizer
que o valor máximo de interesse deve ser buscado nos valores do dicionário.

No caso de empate o valor de saída será o dígito com o valor máximo dos empatados. Neste processo os elementos não
empatados são removidos do dicionário. Depois disso é obtido o valor máximo com a função "max()".
'''

while True: # Loop para cada caso

    # Verifica se é o fim do arquivo
    try:

        n = input() # Entrada do número
    except EOFError:
        break # Condição de saída

    d = {} # Dicionário

    for c in n: # Loop para cada caractere

        if c not in d.keys(): # Caso o dígito não esteja no dicionário

            d[c] = 1 # Inicializa o dígito no dicionário com o valor 1
        else:

            d[c] += 1 # Incrementa o valor da frequencia

    f = max(d, key = lambda k: d[k]) # Valor mais frequente

    c = list(d.values()).count(d[f]) # Quantidade de valores que tem a mesma frequência máxima

    if c > 1: # Caso haja empate de frequencia

        k_del = [] # Lista para deletar as chaves

        for k in d: # Loop para cada chave

            if d[k] != d[f]: # Caso o valor não seja um dos empatatos (não possui o valor igual ao máximo)

                k_del.append(k) # Coloca o valor na lista para deletar
        
        # Deleta o elemento no dicionário
        for k in k_del:

            del d[k]

        print(max(d.keys())) # Exibe o dígito com o maior valor dentre os empatados
    else:

        print(f) # Exibe o dígito mais frequente