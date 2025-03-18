# -*- coding: utf-8 -*-

from math import ceil

# Considerando que a cada dia uma posição é preenchida a quantidade de dias teria que ser o tempo levado para
# preencher a maior distância entre os pontos iniciais. A maneira que estes pontos são preenchidos depende se a
# maior distância está entre dois pontos ou se está entre uma ponta da fita e um ponto. Além disso deve ser
# considerado se há apenas um ponto na fita.

# Para os casos em que há apenas um ponto as distâncias a serem consideradas são entre o início e o fim da fita.

# Para os casos em que há mais de um ponto as distâncias serão entre o início da fita, entre pontos e até o fim
# da fita.

# O tempo demorado para preencher uma distância entre um ponto e uma ponta da fita será a própria distância, neste
# caso se a distância é 10 vão demorar 10 dias para preencher esta seção da fita.

# Quando a distância é de um ponto até outro o número de dias para preencher esta seção será a metade da distância,
# porque cada ponto irá se expandir a cada dia, então com a expanção dos dois a distância entre os espaços preenchidos
# se reduz 2x por dia.

# Para resolver o problema é utilizada uma lista que contêm as distâncias, o primeiro e último elemento correspondem
# as distâncias do íncio a um ponto e do fim a um ponto respectivamente. Todas as outras distâncias são entre pontos.

# Com todas as distâncias computadas é calculado o tempo para preencher cada uma, o maior tempo de todos será o número
# de dias que irá demorar para preencher a fita.

# Variável para o resultado
res = 0

# Lista para as distâncias
dL = []

# Lista para os tempos
t = []

# Input do tamanho da fita e a quantidade de pontos
f, r = map(int, input().split())

# Input das posições
rL = list(map(int, input().split()))

# Caso só exista um ponto
if r == 1:

    # Calcula a distância entre o início da fita e o ponto, depois registra na lista
    dL.append(rL[0] - 1)

    # Calcula a distância entre o fim da fita e o ponto, depois registra na lista
    dL.append(f - rL[0])
# Caso só existam mais de um ponto
else:

    # Loop para cada ponto
    for i in range(r):

        # Caso seja o primeiro ponto
        if i == 0:

            # Calcula a distância entre o início da fita e o ponto, depois registra na lista
            dL.append(rL[i] - 1)
        # Caso seja um ponto intermediário
        elif i != r - 1:

            # Calcula a distância entre o ponto anterior e o ponto atual, depois registra na lista
            dL.append(rL[i] - rL[i - 1] - 1)
        # Caso seja o último ponto
        else:

            # Calcula a distância entre o ponto anterior e o ponto atual, depois registra na lista
            dL.append(rL[i] - rL[i - 1] - 1)

            # Calcula a distância entre o fim da fita e o ponto, depois registra na lista
            dL.append(f - rL[i])

# Loop para o cálculo do tempo
for i in range(len(dL)):

    # Caso a distância seja entre um ponto e uma ponta da fita
    if i == 0 or i == len(dL) - 1:

        # O tempo adicionado é a própria distância
        t.append(dL[i])
    # Caso a distância seja entre pontos
    elif i != len(dL) - 1:

        # O tempo adicionado é a metade da distância, a função "ceil()" é usada para arredondar para cima, corrigindo
        # divisões inexadas
        t.append(ceil(dL[i] / 2))

# O número de dias resultante é o maior tempo demorado
res = max(t)

# Exibe o resultado
print(res)