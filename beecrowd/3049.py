# -*- coding: utf-8 -*-

# input do tamanho b e t.
b = int(input())
t = int(input())

# É possível perceber que as áreas resultantes criam um trapézio.
# Desta forma só é necessário comparar as duas áreas criadas e checar qual é a maior.

# Primeiramente podemos calcular a área da esquerda, sendo que pela fórmula ((B + b) * h) / 2
# as bases serão os valores de b e t. A altura é dada pelo problema como 70 cm.

# Área pertencente a Felix. A área foi convertida de int para float, assim é possível preservar a precisão.
areaF = float(((b + t) * 70) / 2)

# Área pertencente a Marzia. Já que a área da nota é dada por um retângulo 160x70 com área (160 * 70 = 11200 cm^2)
# podemos obter a diferença (Área do retângulo - areaF = areaM).
areaM = 11200 - areaF

# Assim fazemos a comparação se o valor da nota se perdeu.
if areaF == areaM:

    # Escreve 0 no console
    print(0)
# Caso a área de Félix é maior.
elif areaF > areaM:

    # Escreve 1 no console
    print(1)
# Caso a área de Félix é menor só resta uma possibilidade, a que a área de Marzia é maior.
else:

    # Escreve 2 no console
    print(2)