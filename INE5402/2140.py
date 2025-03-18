# -*- coding: utf-8 -*-

'''
A ideia aqui é usar uma função que retorne um valor verdadeiro caso seja possível dar o troco com duas notas.
Para isso a função verifica se o valor pode ser pago com duas vezes a mesma nota de valor menor ou se pode ser 
decomposto em um troco com duas notas.
'''

v = [100, 50, 20, 10, 5, 2]

def calc(t): # Função que determia se o troco pode ser obtido com duas notas

    cn = 0 # Variável que conta a quantidade de notas necessárias
    tmp = t # Variável temporária que armazena o troco durante a sua decomposição

    for c in v:

        # Caso o troco possa ser pago com duas vezes a mesma nota de um valor menor
        # Ex: Duas notas de 10 -> 20 - 10 * 2 == 0
        if t - c * 2 == 0:

            return True

        # Decompõe o valor do troco. Isso é feito subtraindo cada nota enquanto o 
        # troco é maior que aquela nota
        while tmp >= c:

            tmp -= c
            cn += 1
    
    # Caso a contagem das notas da decomposição seja 2 retorna verdadeiro, caso contrário
    # retorna falso
    if cn == 2:

        return True
    else:
        
        return False

while True: # Loop para cada caso

    n, m = map(int, input().split()) # Entrada de n e m

    if n == 0 and m == 0: # Condição de saída
        break
    
    # Chama a função e exibe o resultado
    if calc(m - n):

        print("possible")
    else:

        print("impossible")