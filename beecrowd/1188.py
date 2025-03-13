# -*- coding: utf-8 -*-

""" Ideia: Neste problema é necessário construir uma matriz com os valores de entrada e fazer a operação
especificada no comando S ou M no intervalo especificado. Para fazer isso são usadas as seguintes etapas:

1. Obtenção do comando (S ou M);
2. Criação da matriz;
3. Obtenção dos valores;
4. Cálculo do resultado no intervalo específico, o intervalo das colunas é calculado com base na linha, sendo
que se expande a cada linha.
"""

res = 0         # Variável do resultado

o = input()     # Entrada do comando

mat = [None] * 12           # Inicializa as linhas da matriz
for i in range(12):         # Loop que inicializa cada célula da matriz para cada linha

    mat[i] = [None] * 12

for i in range(12):                     # Itera pelas linhas

    for j in range(12):                 # Itera pelas colunas

        mat[i][j] = float(input())      # Entrada de cada valor da matriz

if o == "S":                            # Caso o comando seja de soma

    for i in range(7, 12):              # Itera pelas linhas da área inferior

        for j in range(12 - i, i):      # Itera pelas colunas da área inferior

            res += mat[i][j]            # Acumula a soma
else:

    for i in range(7, 12):              # Itera pelas linhas da área inferior

        for j in range(12 - i, i):      # Itera pelas colunas da área inferior

            res += mat[i][j] / 30.0     # Acumula a média total

print("{:.1f}".format(res))     # Exibe o resultado