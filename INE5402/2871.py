# -*- coding: utf-8 -*-

''' Ideia: Para chegar aos valores de sacas e litros de café é necessário obter a quatidade total de litros de café.
Isso pode ser obtido com o somatório de todos os elementos da matriz. Esse valor total deve ser dividido para as 
sacas, no caso são usados 60 litros em cada uma então esse valor pode ser dividido por 60 e ter seu resto
desconsiderado. O restante de litros é o próprio resto da divisão dos litros por 60.
'''

while True:                                                         # Loop para os casos

    s = 0                                                           # Variável da soma

    try:                                                            # Detecção do fim do arquivo

        m, n = map(int, input().split())                            # Entradas de m e n
    except EOFError:                                                # Quebra o loop no fim do arquivo
        break

    for _ in range(m):                                              # Loop para cada linha

        s += sum(map(int, input().split()))                         # Faz o somatório da linha

    print("{0} saca(s) e {1} litro(s)".format(s // 60, s % 60))     # Exibe o resultado