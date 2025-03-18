# -*- coding: utf-8 -*-

# O problema pede uma implementação da seguinte lógica:

# 1. Serão dados n valores de x e y que representam os gols.
# 2. O saldo s dos gols deve ser computado com x - y.
# 3. Caso o saldo seja positivo ele é contado como um período, caso contrário ele é descartado e o saldo volta ser 0.
# 4. Enquanto os saldo é positivo (na medida que são adicionados mais valores) o período aumenta.
# 5. Quando o saldo deixa de ser positivo o período acaba.
# 6. O problema pede o valor inicial e final do maior saldo, caso tenha mais de um saldo máximo deve ser usado o que tiver
# o maior período.
# 7. Ainda é pedido que seja exibido "Teste n" no console.
# 8. Caso não tenha nenhum período positivo deve ser exibido "nenhum".

# Para implementar a lógica foi criado um loop while que se repete até que n seja 0. Existe um loop for que processa
# cada partida. Neste loop é obtido o input e é computado o saldo. Caso o saldo seja positivo são registrados o início
# e o fim do período, sendo que o início é registrado apenas quando i é 0 para que não aconteça uma sobreposição do valor
# nas próxima iterações.
# Caso o saldo seja negativo os valores de i e j são "resetados" para 0 juntamente como próprio saldo.
# Caso o saldo desse período que está sendo processado seja o maior saldo registrado até então ele substitui o saldo
# registrado, assim como o i e j substituem o início e o fim do maior período registrado. Caso o haja um saldo igual
# ao maior saldo deste período é verificado se este saldo possui um período maior, caso tenha, os valores de início e fim
# do saldo serão substituidos.

# Quando o loop termina é exibido o teste em questão e caso haja um período positivo é exibido o seu início e fim
# caso contrário é exibido "nenhum".

# Variável para a contagem dos testes.
count = 0

# Loop de cada caso.
while True:

    # Incrementa a contagem.
    count += 1
    
    # Input do n
    n = int(input())

    # Caso o n seja 0 termina o programa.
    if n == 0:
        break

    # Variáveis do início e fim do período, saldo, início e fim do período máximo e saldo máximo.
    i, j, s, maxI, maxJ, maxS = 0, 0, 0, 0, 0, 0

    # Loop que processa cada partida.
    for k in range(n):

        # Input do resultado da partida.
        x, y = map(int, input().split())

        # Somatório e cálculo do saldo.
        s += x - y

        # Caso o saldo seja positivo.
        if s >= 0:

            # Caso seja o início de um período.
            if i == 0:

                # Define o início do período.
                i = k + 1

            # Define o final do período.
            j = k + 1
        else:

            # Reseta o saldo, inicío e fim do período.
            s, i, j = 0, 0, 0
        
        # Checa se o saldo é maior que o maior saldo registrado até então.
        if s > maxS:

            # Substitui o maior saldo e seus valores de início e fim.
            maxS = s
            maxI = i
            maxJ = j
        # Checa se o saldo é igual ao maior saldo e se o seu período é maior ou igual.
        elif s == maxS and j - i >= maxJ - maxI:

            # Substitui os valores de início e fim do período.
            maxI = i
            maxJ = j

    # Escreve "Teste n" no console.
    print("Teste {0}".format(count))

    # Caso haja um período positivo.
    if maxS > 0:

        # Escreve o início e o fim do maior período.
        print("{0} {1}\n".format(maxI, maxJ))
    else:

        # Escreve "nenhum".
        print("nenhum\n")