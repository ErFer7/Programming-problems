# -*- coding: utf-8 -*-

# A idéia para este problema é criar uma lista com os estados da região norte no formato de string, depois disso
# é checado se o estado inserido está contido na lista e é exibido o resultado.

# Lista de estados da ragião norte
rn = ["acre", "amapa", "amazonas", "para", "rondonia", "roraima", "tocantins"]

# Input do estado
e = input()

# Caso o estado esteja na região norte
if e in rn:

    # Exibe o resultado
    print("Regiao Norte")
else:

    # Caso contrário exibe o outro resultado
    print("Outra regiao")