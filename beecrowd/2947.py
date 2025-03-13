# -*- coding: utf-8 -*-

# Para resolver o problema é necessário fazer o somatório de todas as respostas mais frequentes que não sejam as
# mesmas do aluno desafortunado. Já que a maior probabilidade de acertos em uma questão é a de que a resposta mais
# frequente está certa.

# Para isso primeiramente são obtidas as respostas de cada aluno (variável rA) e depois é checado se a resposta é
# a mesma de desafortunado, caso seja a resposta é descartada. Caso contrário a resposta é colocada em um string
# que está em uma lista (lista rQ). Cada string na lista "rQ" representa as respostas dos alunos em uma questão.

# O segundo passo é contabilizar qual é a resposta mais frequente. Para isso é usada duas listas "cList" e "cFreq"
# que representam os caracteres em questão e a frequência dos mesmos respectivamente, a lista "cList" é usada para
# saber qual é o índice que deve ser incrementado na lista de frequência, então se um caractere está no índice "2"
# da "cList" o elemento de índice "2" na "cFreq" vai representar a frequência deste caractere no string.

# Para cada string há um loop que verifica se o caractere está na lista de caracteres "cList", caso esteja o valor 
# de frequência daquele caractere é incrementado na lista "cFreq". Caso contrário esse caractere é adicionado na
# lista "cList" e o valor de frequência "1" é adicionado na "cFreq".

# Depois disso é adicionado ao resultado o valor mais alto na lista de frequências.

# Variável do resultado
res = 0

# Input da quantidade de questões na prova
k = int(input())

# Lista para os strings com as respostas
rQ = [""] * k

# Input das respostas de desafortunado
rD = input()

# Input da quantidade de alunos
n = int(input())

# Loop para as respostas de cada aluno
for _ in range(n):

    # Input das respostas do aluno
    rA = input()

    # Loop que vai verificar se as respostas são iguais as do desafortunado
    for i in range(len(rA)):

        # Caso os caracteres sejam diferentes
        if rA[i] != rD[i]:

            # Adciona o caractere no string da questão
            rQ[i] += rA[i]

# Loop que verifica qual é a resposta mais frequente de uma questão
for s in rQ:

    # Lista para os caracteres
    cList = []

    # Lista para a frequência dos caracteres
    cFreq = []

    # Para cada caractere no string
    for c in s:

        # Caso o caractere esteja na lista de caracteres
        if c in cList:

            # Incrementa a frequência do caractere
            cFreq[cList.index(c)] += 1
        else:

            # Caso o caractere não esteja na lista ele é acidicionado na mesma
            cList.append(c)
            
            # Incrementa a frequência do caractere
            cFreq.append(1)
    
    # Checa se a lista não está vazia
    if len(cFreq) > 0:

        # Soma o valor mais frequente ao resultado
        res += max(cFreq)

# Exibe o resultado
print(res)