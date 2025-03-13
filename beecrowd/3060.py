# -*- coding: utf-8 -*-

# A ideia neste código é obter o quociente e o resto da divisão, com isso é pode-se criar um loop em que as
# parcelas são processadas e exibidas. Caso a divisão seja inexata será adicionado 1 ao valor da parcela,
# ao mesmo tempo é descontado 1 do valor do resto da divisão Este processo é repetido enquanto o resto é maior
# que 0.

# Valor do produto e parcelas.
v = int(input())
p = int(input())

# Quociente do valor dividido pelas parcelas.
pB = v // p
# Resto da divisão do valor pelas parcelas.
pA = v % p

# Loop que processa o valor de cada parcela.
for i in range(p):

    # Caso a divisão não seja exata o resto será maior que 0, executando o bloco abaixo.
    if pA > 0:

        # É descontado os valores que já foram distribuidos nas parcelas.
        pA -= 1
        # Escreve no console o valor da parcela, considerando a distribuição.
        print(pB + 1)
    # No caso de divisão exata o resto é 0, executando o bloco abaixo.
    else:

        # Escreve no console o valor da parcela sem a distribuição.
        print(pB)