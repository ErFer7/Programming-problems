# -*- coding: utf-8 -*-

''' Ideia: No problema é usado um loop que irá verificar qual é a posição de cada caractere do texto em um alfabeto
normal. Com essa posição basta verificar qual é o caractere correspondente no alfabeto permutado. O resultado é
adicionado a um string.
'''

a = "abcdefghijklmnopqrstuvwxyz"    # Alfabeto normal
res = ""                            # Variável para o resultado

p = input()                         # Entrada do alfabeto permutado
x = input()                         # Entrada do texto cifrado

for c in x:                         # Loop que itera sobre cada caractere do texto

    res += p[a.index(c)]            # Adiciona no resultado o caractere correspondente no alfabeto permutado

print(res)                          # Exibe o resultado