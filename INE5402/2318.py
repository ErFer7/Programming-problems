# -*- coding: utf-8 -*-

'''
Para completar os números é necessário obter a soma que as linhas, colunas e diagonais deveriam gerar. Assim
a variável "n" irá armazenar este número. Primeiramente é obtida a matriz e feita a soma total dos elementos.

Para cada linha, coluna e diagonal é checado se a mesma não possui zeros, caso não tenha o número "n" será o somatório
desta linha, coluna ou diagonal. Caso ela seja apenas preenchida de zeros o valor de "n" será a metade do somatório
total. Essa relação acontece porque o somatório total dos elementos sempre seria "3 * n" já que temos 3 linhas e 3 colunas.
Caso alguma coluna, linha ou diagonal seja removida ficamos com "2 * n".

A variável "nDef" é usada para checar se "n" já está definido.

Com o "n" determinado é usado um loop que tem "z" iterações ("z" = quantidade de zeros). Para cada iteração os zeros são
substituidos pelo número correto. Neste caso quando um zero é encontrado é feita a operação para determinar o número que falta.
No caso essa operação deve ser a diferença entre "n" e o somatório da linha. A mesma operação é repetida para a 
coluna, garantindo que o resultado estará certo.
'''

mat = []            # Matriz do quadrado
z = 0               # Quantidade de zeros
n = 0               # Número mágico
tN = 0              # Somatório do quadrado
nDef = False        # Variável para checar se "n" já está definido

for i in range(3):                          # Loop para cada linha do quadrado

    ln = list(map(int, input().split()))    # Entrada de cada linha do quadrado

    z += ln.count(0)                        # Soma a quantidade de zeros

    mat.append(ln)                          # Adiciona a linha na matriz
    tN += sum(ln)                           # Somatório total da matriz

for i in range(3):                                                  # Loop para cada linha

    if mat[i][0] != 0 and mat[i][1] != 0 and mat[i][2] != 0:        # Verifica se não a zeros na linha

        n = mat[i][0] + mat[i][1] + mat[i][2]                       # Determina "n"
        nDef = True                                                 # Define "n" como determinado
        break                                                       # Quebra o loop
    elif mat[i][0] == 0 and mat[i][1] == 0 and mat[i][2] == 0:      # Caso a linha tenha apenas zeros

        n = tN // 2                                                 # Determina "n"
        nDef = True                                                 # Define "n" como determinado
        break                                                       # Quebra o loop

if not nDef:                                                            # Caso "n" ainda não esteja definido

    for i in range(3):                                                  # Loop para cada coluna

        if mat[0][i] != 0 and mat[1][i] != 0 and mat[2][i] != 0:        # Verifica se não a zeros na coluna

            n = mat[0][i] + mat[1][i] + mat[2][i]                       # Determina "n"
            nDef = True                                                 # Define "n" como determinado
            break                                                       # Quebra o loop
        elif mat[0][i] == 0 and mat[1][i] == 0 and mat[2][i] == 0:      # Caso a coluna tenha apenas zeros

            n = tN // 2                                                 # Determina "n"
            nDef = True                                                 # Define "n" como determinado
            break                                                       # Quebra o loop

if not nDef:                                                        # Caso "n" ainda não esteja definido

    if mat[0][0] != 0 and mat[1][1] != 0 and mat[2][2] != 0:        # Verifica se não a zeros na diagonal

        n = mat[0][0] + mat[1][1] + mat[2][2]                       # Determina "n"
        nDef = True                                                 # Define "n" como determinado
    elif mat[0][0] == 0 and mat[1][1] == 0 and mat[2][2] == 0:      # Caso a diagonal tenha apenas zeros

        n = tN // 2                                                 # Determina "n"
        nDef = True                                                 # Define "n" como determinado

if not nDef:                                                        # Caso "n" ainda não esteja definido

    if mat[0][2] != 0 and mat[1][1] != 0 and mat[2][0] != 0:        # Verifica se não a zeros na diagonal oposta

        n = mat[0][2] + mat[1][1] + mat[2][0]                       # Determina "n"
        nDef = True                                                 # Define "n" como determinado
    elif mat[0][2] == 0 and mat[1][1] == 0 and mat[2][0] == 0:      # Caso a diagonal oposta tenha apenas zeros

        n = tN // 2                                                 # Determina "n"
        nDef = True                                                 # Define "n" como determinado

for _ in range(z):                                                     # Loop para cada zero

    for i in range(3):                                                 # Loop para linhas

        for j in range(3):                                             # Loop para cada número

            if mat[i][j] == 0:                                         # Caso o número seja zero

                mat[i][j] = n - mat[i][0] - mat[i][1] - mat[i][2]               # Determina o número

                if mat[i][0] + mat[i][1] + mat[i][2] == n:                      # Checa se o somatório está correto
                    
                    if mat[i][0] != 0 and mat[i][1] != 0 and mat[i][2] != 0:    # Checa se não há zeros na linha

                        continue                                                # Continua para a próxima iteração

                    mat[i][j] = 0                                               # Redefine o número (Caso de falha do cálculo)

                mat[i][j] = n - mat[0][j] - mat[1][j] - mat[2][j]               # Determina o número

                if  mat[0][j] + mat[1][j] + mat[2][j] == n:                     # Checa se o somatório está correto

                    if mat[0][j] != 0 and mat[1][j] != 0 and mat[2][j] != 0:    # Checa se não há zeros na coluna

                        continue                                                # Continua para a próxima iteração

for i in range(3):                                                  # Loop para cada linha

    print("{0} {1} {2}".format(mat[i][0], mat[i][1], mat[i][2]))    # Exibe cada linha