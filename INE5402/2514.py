# -*- coding: utf-8 -*-

'''
Neste problema para encontrar o próximo ano em que acontece o alinhamento dos planetas é necessário encontrar
o periodo em que eles se alinham. Isso é possível calculando o mínimo múltiplo comum entre os valores fornecidos.

Ex: l = 1, 2, 3

Os números inteiros representam as posições alinhadas entre o planeta e a estrela. Cada número representa uma orbita
da lua mais próxima, em que seu valor é o número de voltas.

l1: 0 1 2 3 4 5 6
l2: 0 1/2 1 3/2 2 5/2 3
l3: 0 1/3 2/3 1 4/3 5/3 2

Percebe-se que na última posição todos são inteiros, significando que se alinharam. Esta é a posição que é
determinada pelo mmc.

Depois disso é feita a diferença entre o ano do último alinhamento e o próximo, assim se obtém quantos anos restam
para as luas se alinharem.

O mmc é calculado usando o mdc, neste caso a fórmula é a * b / mdc(a, b). Isso torna a execução mais eficiente.
'''

def mdc(a, b): # Função do mdc

    if b == 0: # Caso o valor tenha sido determinado

        return a
    else:

        return mdc(b, a % b) # Calcula recursivamente o mdc

# Função do mmc
def mmc(a, b):

    return a * b // mdc(a, b)

while True: # Loop para cada caso

    # Detecta o fim do arquivo
    try:

        m = int(input()) # Entrada de m
    except EOFError:
        break

    l1, l2, l3 = map(int, input().split()) # Entrada do periodo orbital das luas

    p = mmc(l1, mmc(l2, l3)) # Determina o periodo dos alinhamentos (mmc dos 3 valores)

    print(p - m) # Exibe a diferença que será o tempo restante para o próximo alinhamento