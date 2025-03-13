# -*- coding: utf-8 -*-

# Neste código o texto é registrado na variável "s". Usando a função "maketrans()" é possível fazer uma tabela de
# tradução, em que o string "@&!*#" representa os caracteres que serão substituídos pelos caracteres do string
# "aeiou". A substituição é feita na ordem do string, ou seja "@" significa "a".

# Usando a tabela de tradução é possível chamar a função "translate()" que recebe a tabela como argumento.
# O resultado da função é diretamente exibido.

# Loop para os casos
while True:

    # Verifica se é o fim do texto
    try:

        # Input do string "s"
        s = input()

        # Faz a tabela de tradução "t"
        t = str.maketrans("@&!*#", "aeiou")

        # Traduz o string e exibe o resultado
        print(s.translate(t))
    except EOFError:
        break