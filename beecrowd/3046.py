# -*- coding: utf-8 -*-

'''
A solução aqui é simples. Basta usar a fórmula informada para calcular a quantidade de peças. Usei uma função para
aplicar um pouco do conteúdo.
'''

def qtepec(N): # Função que calcula a quantidade de peças

    return ((N + 1) * (N + 2)) // 2 # Retorna o resultado

N = int(input()) # Entrada de N

print(qtepec(N)) # Exibe o resultado
