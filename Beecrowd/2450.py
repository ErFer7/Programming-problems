# -*- coding: utf-8 -*-

''' Ideia: Neste problema é usada uma variável (index) para o controle da matriz. O conceito é que essa variável
armazena o índice do elemento a esquerda do início dos números em uma linha. No caso se uma linha começa a ter
números diferentes de 0 no índice 3 a matriz só será escada se os números de índice 2 a 0 forem 0. A verificação
compara se a variável index é maior ou igual ao índice em questão (caso o número seja diferente de 0), caso seja
a matriz não é escada.

Essa variável é incrementada de acordo com a posição em que começam os números na matriz ou em alguns casos quando
a linha muda.
'''

index = -1                          # Variável index
v = True                            # Variável que marca de a matriz é escada ou não

n, m = map(int, input().split())    # Entrada de n e m

for _ in range(n):                          # Loop que itera por cada linha

    ln = list(map(int, input().split()))    # Entrada da linha

    if v:                                   # Caso a matriz ainda seja válida

        s = False                           # Variável que marca se a linha já começou a ter números diferentes de 0
        c = False                           # Varióvel que marca se index já foi incrementado

        for i in range(m):                  # Loop para cada número

            if ln[i] != 0:                  # Caso o número seja diferente de 0

                s = True                    # Marca a linha como "iniciada"

                if i <= index:              # Verifica se a linha desrespeita a regra da matriz escada

                    v = False               # Marca a matriz como inválida
                                
                break                       # Quebra o loop
            elif not s and i > index:       # Caso a linha não tenha começado e o índice é maior que index

                index += 1                  # Incrementa o index
                c = True                    # Marca o index como incrementado para evitar que ele seja incrementado na mudança de linha
        
        if not c:                           # Caso o index não tenha sido incrementado em nenhuma situação

            index += 1                      # Incrementa o index

if v:               # Caso a matriz seja válida

    print('S')      # Exibe o resultado
else:               # Caso contrário

    print('N')      # Exibe o resultado