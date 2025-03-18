# -*- coding: utf-8 -*-

''' Ideia: Para resolver este problema cada coluna é analizada em um loop. Uma lista "cols" é criada e armazena o
valor verdadeiro quando há alunos em uma coluna ou falso caso contrário. Caso os valores verdadeiros se repitam em
sequência a sala é inválida.

    Quando uma coluna têm alunos é feita a verificação da distância entre alunos com a mesma prova. Então caso o
valor na posição não seja 0 é checado se o índice do próximo aluno com a mesma prova menos o índice atual é menor 
ou igual a distância válida.

    Depois das verificações feitas o resultado é exibido.
'''

mat = []                                # Matriz para a turma
res = True                              # Variável para o resultado

n, m, c = map(int, input().split())     # Entrada de n, m e c

cols = [False] * m                      # Lista para as colunas

for _ in range(n):                                  # Loop da entrada da matriz

    mat.append(list(map(int, input().split())))     # Entrada de cada linha da matriz

for i in range(m):      # Loop para cada coluna

    if res:             # Verifica se a sala ainda é válida e o programa deve ser continuado

        col = []        # Lista para a coluna
        for j in range(n):              # Loop para cada elemento da coluna

            if mat[j][i] != 0:          # Caso esta coluna tenha algum aluno

                cols[i] = True          # Classifica que a coluna têm alunos

            col.append(mat[j][i])       # Adiciona os elementos na coluna

        if i > 0 and cols[i - 1] and cols[i]:       # Caso não seja a primeira coluna e duas colunas tenham alunos em seguida

            res = False                             # Marca a sala como inválida
            break                                   # Quebra o loop

        if cols[i]:                                                 # Caso a coluna atual tenha alunos
            
            for j in range(n - 1):                                  # Loop para os elementos da coluna menos último
                    
                if col[j] != 0:                                         # Caso tenha um aluno nesta posição

                    try:                                                # A checagem de erro é feita para evitar que col.index(col[j], j + 1) falhe caso não tenha o número adiante na coluna

                        if col.index(col[j], j + 1) - j <= c:           # Caso a distância entre os alunos não seja valida

                            res = False                                 # Marca a sala como inválida
                            break                                       # Quebra o loop
                    except ValueError:                                  # Captura o erro
                        continue                                        # Continua caso col.index(col[j], j + 1) dê erro
    else:               # Caso a sala não seja mais válida quebra o loop
        break

if res:             # Caso a sala seja válida

    print('S')      # Exibe o resultado
else:               # Caso contrário

    print('N')      # Exibe o resultado