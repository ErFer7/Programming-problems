# -*- coding: utf-8 -*-

# Neste código é processada quantidade de placas possíveis dada uma quantidade de consoantes e digitos.
# Com a definição de arranjo com repetição que as combinações possíveis são n^p podemos calcular as possibilidades
# de cada parte da placa (consoantes e dígitos) da placa, sendo que n é 26 para consoantes e 10 para dígitos
# e o p é dado pelo input c e d. Depois basta multiplicar as possibilidades das consoantes pelas dos dígitos para
# obter a possibilidade de placas.

# Mesmo assim ainda existe um problema quando c e d são 0. Pelo arranjo o resultado seria 1 porém isso não é
# possível, então neste caso foi definido que quando c e d são 0 o resultado será sempre 0.

# Número de instâncias.
n = int(input())

# Loop que processa cada input de c e d.
for i in range(n):

    # Input do c e d. O input é separado em um vetor de 2 elementos, esse vetor é mapeado com a função map()
    # aplicando a função int() nos 2 elementos, depois o mapa é convertido em uma lista.
    cd = list(map(int, input().split()))

    # Caso pelo menos c ou d sejam diferentes de 0 o resultado será dado pela operação específicada.
    if cd[0] != 0 or cd[1] != 0:

        # Escreve no console as possibilidades de placas dada por (26^c * 10^d)
        print(26**cd[0] * 10**cd[1])
    # Caso o c e d sejam 0 o resultado será sempre 0
    else:

        # Escreve 0 no console
        print(0)