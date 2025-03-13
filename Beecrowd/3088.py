# -*- coding: utf-8 -*-

# Neste problema é usada a função "replace()" para substituir as partes do string que são " ," e " .".
# O string é registrado na variável "s" e depois é usada a função replace para cada um dos dois casos.
# No fim o resultado é exibido

# Loop para cada caso
while True:

    # Checa se é o fim do texto
    try:

        # Input do variável "s"
        s = input()

        # Substitui todos os strings " ," por "," removendo os espaços
        s = s.replace(" ,", ",")

        # Substitui todos os strings " ." por "." removendo os espaços
        s = s.replace(" .", ".")

        # Exibe o resultado
        print(s)
    except EOFError:
        break