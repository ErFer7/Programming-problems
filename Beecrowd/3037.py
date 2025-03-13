# -*- coding: utf-8 -*-

# O processo envolve criar um loop para os casos de teste e um loop para cada arremesso. Com isso são computados
# os somatórios das pontuações, depois disso as pontuações são comparadas e o resultado é exibido.

# Número de casos de teste
n = int(input())

# Loop do caso de teste, cada iteração do loop corresponde a um caso de teste
for i in range(n):

    # Pontuação de João e Maria
    joao = 0
    maria = 0

    # Loop de cada arremesso
    for j in range(6):

        # Input dos arremssos. O input é separado em um vetor de 2 elementos, esse vetor é mapeado com a função map()
        # aplicando a função int() nos 2 elementos, depois o mapa é convertido em uma lista.
        xd = list(map(int, input().split()))

        # 3 primeiros arremessos
        if j < 3:

            # Registra o somatório de pontos de João como a pontuação vezes a distância
            joao += xd[0] * xd[1]
        # 3 últimos arremessos
        else:

            # Registra o somatório de pontos de Maria como a pontuação vezes a distância
            maria += xd[0] * xd[1]
    
    # Caso João tenha mais pontos que maria a vitória é de João
    if joao > maria:

        # Escreve JOAO no console
        print("JOAO")
    # Já que o problema não específicou a condição de empate a única outra possíbilidade é a de vitória de Maria
    else:

        # Escreve MARIA no console
        print("MARIA")