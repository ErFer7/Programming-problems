# -*- coding: utf-8 -*-

'''Ideia: Para resolver o problema é necessário encontrar o intervalo na lista o qual tenha a maior soma. Isso
pode ser resolvido com o algoritmo de Kadane (https://en.wikipedia.org/wiki/Maximum_subarray_problem). O funcionamento
é o seguinte:

1. Os valores da soma total (tMax) e soma atual são inicializados (cMax);
2. O valor da lista no índice i do loop é adicionado na soma atual (cMax);
3. Caso a soma atual (cMax) seja maior que a maior soma já registrada (tMax) então a soma total é substituida pela
soma atual;
4. Caso a soma atual (cMax) seja negativa ela será zerada. Já que isso significa que o intervalo não será o maior
de qualquer jeito. Caso cMax seja maior ou igual a 0 a sua soma continua;
5. O resultado é obtido com a soma máxima (tMax).

Obs: Embora o problema seja simples eu resolvi incluir o algoritmo aqui porque entendi a solução melhor com ele.
'''

tMax = -100     # Variável da soma total inicializada com um valor que sempre será substituido na primeira iteração
cMax = 0        # Variável da soma atual

n = int(input())                        # Entrada de n
v = list(map(int, input().split()))     # Entrada da lista
       
for i in range(n):      # Loop que itera pelos valores da lista

    cMax += v[i]        # Soma o valor da lista na soma atual

    if (cMax > tMax):   # Caso a soma atual seja a maior registrada até o momento

        tMax = cMax     # Substitui a soma máxima pela soma atual

    if cMax < 0:        # Caso a soma atual seja negativa

        cMax = 0        # Descarta a soma

print(tMax)     # Exibe o resultado