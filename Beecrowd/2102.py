# -*- coding: utf-8 -*-

''' Ideia: Neste problema é usado um dicionário que irá registrar os valores do somatório. No caso a chave é um
tuple feito a partir do endereço na matriz fornecido e o valor do dicionário é o somatório dos valores naquele
endereço.

Obs: foi usado um tuple em vez de um string para facilitar a organização do dicionário

No fim do processo os itens do dicionário são organizados em ordem crescente e exibidos conforme o especificado.
Os itens são primeiramentes retirados do dicionário para que possam ser organizados.
'''

t = int(input())    # Entrada de t

for i in range(t):                      # Loop para cada caso

    d = {}                              # Dicionário

    n, l = map(int, input().split())    # Entradas de n e l

    for _ in range(l):                          # Loop para cada linha

        ln = input().split()                    # Entrada da linha
        
        k = tuple(map(int, [ln[1], ln[2]]))     # Cria um tuple (chave) a partir do endereço do valor (linha e coluna)

        vk = int(ln[3])                         # Converte o valor para inteiro

        if k not in d.keys():                   # Caso esta chave não tenha sido usado antes

            d[k] = vk                           # Cria um novo item no dicionário com o valor
        else:                                   # Caso contrário

            d[k] += vk                          # Adiciona o valor na chave

    it = d.items()                              # Obtém os itens do dicionário em forma de vetores
    res = sorted(it)                            # Organiza em ordem crescente

    for r in res:                                               # Loop para cada somatório

        print("{0} {1} {2}".format(r[0][0], r[0][1], r[1]))     # Exibe o somatório
    
    if i != t - 1:      # Verifica se não é o último caso

        print('')       # Espaço extra