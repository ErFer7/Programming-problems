# -*- coding: utf-8 -*-

# O código funciona descontando gastos e adicionando ganhos a uma variável de saldo. Cada valor citado é 
# adicionado ou descontado ao saldo da UFSC, no final é checado se o saldo é negativo, positivo ou igual a 0. 
# Quando o saldo é posivivo ou igual a 0 a greve para, caso contrário ela continua.

# Variável de saldo da UFSC
s = 0

# Número de valores citados
n = int(input())

# Loop que processa os valores
for i in range(n):

    # O input é dividido em um vetor com 2 elementos
    tc = input().split()

    # Define t como o primero elemento do vetor 
    t = tc[0]
    # Converte o valor para inteiro
    c = int(tc[1])

    # Caso o caractere seja V o valor é um ganho, sendo assim adicionado ao saldo
    if t == "V":

        # Adiciona o valor do saldo
        s += c
    # Caso o caractere não seja V ele só pode ser G, ou seja um ganho. Com isso o valor é descontado
    else:

        # Desconta o valor do saldo
        s -= c

# Checa se o saldo é positivo ou igual a 0
if s >= 0:

    # Escreve no console que a greve vai parar. Já que há dinheiro suficiente para a universidade
    print("A greve vai parar.")
# Caso o saldo seja negativo
else:

    # Escreve no console que a greve vai continuar. Já que não há dinheiro suficiente
    print("NAO VAI TER CORTE, VAI TER LUTA!")