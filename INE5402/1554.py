# -*- coding: utf-8 -*-

# Para resolver este problema existem 2 loops, um loop se trata de cada caso de teste e o outro de cada bola.
# No loop para cada bola é obtida as coordenadas de todas elas, incluindo a da bola branca. Depois disso é
# checado se a bola é branca, no caso isso é feito checando se as coordenadas são as primeiras do loop.
# Caso a bola seja a branca as suas coordenadas x e y serão registradas nas variáveis wBX e wBY. Caso a bola
# não seja a branca ela terá a sua distância em relação a branca calculada e comparada com a menor distância já
# registrada. Na primeira comparação o valor de dMin sempre será substituido pois nenhuma bola terá uma distância
# maior que 3200.0 mm, por isso mesmo a variável dMin foi declarada com este valor. Quando a substituição acontece
# o índice da bola também é registrado na variável iP.

# Importa a função sqrt do módulo math.
from math import sqrt

# Número de casos de teste.
n = int(input())

# Loop de cada caso de teste.
for i in range(n):

    # Número de bolas.
    nB = int(input())

    # Cordenadas da bola branca.
    wBX, wBY = 0.0, 0.0
    # Menor distância entre bolas (declarada com um valor máximo por causa da forma que são comparadas as distâncias).
    dMin = 3200.0
    # Índice ou posição da bola mais próxima.
    iP = 0

    # Loop que processa a distância de cada bola.
    for j in range(nB + 1):

        # Input de x e y. O input é separado em um vetor de 2 elementos, esse vetor é mapeado com a função map()
        # aplicando a função float() nos 2 elementos, depois o mapa é convertido em uma lista.
        xy = list(map(float, input().split()))

        # Caso seja a primeira bola, ou seja a branca.
        if j == 0:

            # Registra as cordenadas X e Y da bola branca.
            wBX = xy[0]
            wBY = xy[1]
        else:

            # Calcula a distância entre a bola branca e a bola com a definição da distância entre 2 pontos.
            d = sqrt((xy[0] - wBX)**2 + (xy[1] - wBY)**2)

            # Se a distância for menor que a menor distância registrada até então.
            if d < dMin:
                
                # Substitui a distância pela nova distância menor.
                dMin = d
                # Registra o índice ou posição da bola.
                iP = j
    
    # Escreve o índice da bola mais próxima da branca no console.
    print(iP)