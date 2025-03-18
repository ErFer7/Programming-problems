# -*- coding: utf-8 -*-

# Neste problema é possível perceber um certo padrão. Quando não há a repetição dos comandos é possível considerar
# que a cada comando executado o número de passos que vem depois aumtentam em 1. Sendo assim a sequência "1, 2, 3"
# significaria que o resultado seria 1 + (2 + 1) + (3 + 2*1). Pois depois que o primeiro comando fosse executado 
# seriam necessários mais um toque extra na tecla para chegar na mesma posição, isso se repete com todos os comandos
# caso eles não se repitam.

# Quando há uma repetição basta pressionar a tecla o número de vezes suficientes para chegar até a última posição que
# o comando foi pressionado. Então na sequência "1, 2, 1" até o 2 a lógica normal seria aplicada, porém quando há
# o 1 novamente pode se considerar que o comando foi executado a 2 passos atrás. Então pode-se considerar que o
# número de passos é o índice do comando a ser executado na lista fornecida menos o índice da última vez que esse
# mesmo comando apareceu na lista. No programa foi usada uma lista como histórico para contabilizar a repetição de
# comandos.

# Loop para os casos
while True:

    # Variável do resultado
    res = 0

    # Lista que armazena o histório de comandos que estão sendo executados
    ex = []

    # Input do número de comandos
    n = int(input())

    # Condição de saída
    if n == 0:
        break

    # Lista de comandos
    cmd = list(map(int, input().split()))

    # Loop que itera por cada comando
    for i in range(len(cmd)):

        # Caso o comando tenha se repetido (se está no histórico)
        if cmd[i] in ex:

            # É calculada a última vez que esse comando foi executado e consequentemente o número de passos
            res += i - ex.index(cmd[i])

            # Substitui o comando no histórico por 0, assim é evitado que o resultado falhe caso tenham várias
            # repetições. O comando não poderia ser removido do histório porque isso iria mudar os índices e
            # com isso o resultado seria incorreto
            ex[ex.index(cmd[i])] = 0

            # Adiciona o comando no histórico
            ex.append(cmd[i])
        else:

            # Calcula o número de passos conforme explicado no primeiro comentário
            res += cmd[i] + i

            # Adiciona o comando no histórico
            ex.append(cmd[i])

    # Exibe o resultado
    print(res)