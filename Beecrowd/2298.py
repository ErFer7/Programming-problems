# -*- coding: utf-8 -*-

# O problema é resolvido com as condições específicas de cada regra. Os comentários acima das regras explicam
# o seu funcionamento

# Variável para a contagem dos testes
count = 0

# Input do número de casos
n = int(input())

# Loop para cada caso
for _ in range(n):

    # Resultado da pontuação
    res = 0

    # Lista de números que representam as cartas
    cList = list(map(int, input().split()))

    # Sorteia os números em ordem crescente
    cList.sort()

    # Condição de sequência
    # Para a condição de sequência é usada uma variável "seq" que é verdadeira caso exista uma sequência de cartas.
    # Para verificar a condição é usado um loop que verifica se as cartas a partir do valor mínimo não concidem com 
    # o índice do loop (os valores são corrigidos para o intervalo 0 a 5 com a operação "número da carta" - "mínimo").
    
    # Variável da sequência
    seq = True

    # Loop para a verificação
    for i in range(5):

        # Caso a carta x (Neste caso x - carta mínima) seja diferente do índice do loop
        if cList[i] - min(cList) != i:

            # As cartas não formam uma sequência
            seq = False
            break

    # Caso as cartas formem uma sequência a pontuação é calculada
    if seq:

        res = 200 + min(cList)

    # Condição de quadra
    # Nesta condição caso o resultado já não tenha sido calculado é feita a verificação. Já que só 2 valores podem
    # existir nessa condição pode ser usado o mínimo e o máximo na verificação. Para os dois valores é verificado se
    # a contagem na lista é 4, caso seja é calculada a pontuação

    if res == 0:

        # Caso o valor mínimo se repete 4 vezes calcula a pontuação
        if cList.count(min(cList)) == 4:

            res = 180 + min(cList)
        # Caso o valor máximo se repete 4 vezes calcula a pontuação
        elif cList.count(max(cList)) == 4:
        
            res = 180 + max(cList)
    
    # Condição de trinca e par e apenas trinca

    # Caso o resultado não tenha sido calculado ainda
    if res == 0:

        # Condição de trinca e par

        # Novamente são considerados apenas dois valores usando o máximo e o mínimo. Neste caso é verificado se o
        # mínimo tem a contagem 3 e o máximo 2 ou vice versa. Caso essa condição seja verdadeira é verificado qual
        # é a carta da trinca e qual é a do par (mínimo ou máximo), depois é calculada a pontuação

        # Condição se o valor máximo e mínimo tem a contagem 3 e 2 ou ao contrário
        if (cList.count(min(cList)) == 3 and cList.count(max(cList)) == 2) or (cList.count(min(cList)) == 2 and cList.count(max(cList)) == 3):

            # Caso a contagem do mínimo seja maior calcula a pontuação com base neste valor
            if cList.count(min(cList)) == 3:

                res = 160 + min(cList)
            # Caso a contagem do máximo seja maior calcula a pontuação com base neste valor
            elif cList.count(max(cList)) == 3:

                res = 160 + max(cList)

        # Condição de apenas trinca

        # Caso a condição anterior falhe nos pares será checado se há uma trinca. Já que agora existem 3 valores
        # diferentes não podem ser usados os mínimos e os máximos. Com isso há um loop que checa cada carta e
        # verifica se há 3 instâncias dessa carta na lista.

        else:

            # Loop que itera por cada carta
            for c in cList:

                # Caso a contagem dessa carta seja 3
                if cList.count(c) == 3:

                    # Calcula a pontuação
                    res = 140 + c
                    break

    # Condição de pares

    # Nesta condição é usada uma variável "p" para contar quantos pares existem na lista, e mais duas variáveis
    # "c1" e "c2" que representam os valores dos pares. Um loop é usado para checar se a contagem daquela carta é 2
    # ou seja a carta forma um par, caso dois pares se formem é calculado o valor da pontuação para este caso. Caso
    # contrário é calculado o valor da pontuação para o caso de apenas um par.

    if res == 0:

        # Variável para a quantidade de pares
        p = 0
        
        # Variáveis para os valores de cada par
        c1, c2 = 0, 0

        # Loop para a checagem
        for c in cList:

            # Caso a contagem da carta é 2
            if cList.count(c) == 2:

                # Caso este seja o primeiro par
                if p == 0:
                    
                    # Coloca o valor da carta no valor do primeiro par
                    c1 = c

                    # Incrementa a contagem de pares
                    p += 1
                # Caso o valor seja de um par de cartas e este valor já não foi colocado nas variáveis c1 e c2
                elif c != c1 and c != c2:

                    # Coloca o valor da carta no valor do segundo par
                    c2 = c

                    # Incrementa a contagem de pares
                    p += 1

        # Condição de dois pares
        if p == 2:

            # Checa qual é o maior par e calcula a pontuação
            if c1 > c2:

                res = 3 * c1 + 2 * c2 + 20
            else:

                res = 3 * c2 + 2 * c1 + 20
        # Condição de apenas um par
        elif p == 1:

            # Calcula a pontuação de apenas um par
            res = c1 
    
    # Incrementa a contagem de testes
    count += 1

    # Exibe o resultado
    print("Teste {0}\n{1}\n".format(count, res))