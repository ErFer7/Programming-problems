# -*- coding: utf-8 -*-

# A idéia é checar quantos números da lista da aposta de flavinho estão incluidos na lista de resultados do
# sorteio.

# Variável do resultado
res = 0

# Input da lista da aposta de flavinho
f = input().split()

# Input da lista de resultados do sorteio
r = input().split()

# Loop que itera na lista de flavinho
for i in f:

    # Checa se o número apostado está na lista de sorteios
    if i in r:

        # Incrementa o número de números acertados
        res += 1

# Condições para cada quantidade de números acertados
if res == 6:

    print("sena")
elif res == 5:

    print("quina")
elif res == 4:

    print("quadra")
elif res == 3:

    print("terno")
else:

    print("azar")