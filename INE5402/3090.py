# -*- coding: utf-8 -*-

'''
O rio pode ser considerado como uma linha que vai do 0, 0 até n, m. Neste caso a inclinação da linha pode
ser obtida como o coeficiente angular de uma reta "y = ax + b" que seria "y / x". No caso do problema isso seria
"n / m". Sendo assim o rio passa pela linha "y * (n / m)" para o soldado na coluna "y". Com isso podemos verificar
se a linha "x" está acima ou abaixo da linha do rio na coluna "y".

Após a verificação é feito o somatório e no fim do programa o resultado é exibido.
'''

e0, e1 = 0, 0                           # Variáveis para o somatório do primeiro e segundo exército

n, m, s = map(int, input().split())     # Entradas de n, m e s

coef = n / m                            # Coeficiente angular da linha do rio

for _ in range(s):                          # Loop para cada soldado

    x, y, h = map(int, input().split())     # Entrada de x, y e h

    if x < y * coef:                        # Caso o soldado esteja acima do rio

        e0 += h                             # Faz o somatório para o primeiro exército
    else:                                   # Caso o soldado esteja abaixo do rio

        e1 += h                             # Faz o somatório para o segundo exército

print("{0} {1}".format(e0, e1))     # Exibe o resultado