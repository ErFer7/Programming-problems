# -*- coding: utf-8 -*-

# Neste problema cada valor de horário é checado no loop, assim é computada a quantidade de alunos que chegaram
# no horário correto. Depois disso é feita a comparação com a quantidade mínima de alunos necessários.

# Input da quantidade de alunos e quantidade mínima de alunos para o início da aula
n, k = map(int, input().split())

# Input da lista de horários
v = list(map(int, input().split()))

# Variável da quantidade de alunos que foram pontuais
a = 0

# Loop que itera na lista
for s in v:

    # Checa se o aluno foi pontual
    if s <= 0:

        # Incrementa a quantidade de alunos que foram pontuais
        a += 1

# Checa se há alunos suficientes para o início da aula e exibe o resultado do problema
if a >= k:

    print("YES")
else:

    print("NO")