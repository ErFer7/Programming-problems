# -*- coding: utf-8 -*-

'''
Para resolver o problema é necessário considerar todas as posições da matriz primeiro. Para isso são
usadas duas funções de tranformação de matrizes, a função de rotação e uma de espelhamento.

O programa compara cada elemento em cada matriz com a função "comp_mat" que retorna a precisão.

A matriz que está sendo testada é rotacionada para os quatro possíveis lados e para cada rotação é comparada 
novamente com a matriz padrão. Depois disso ela é espelhada e rotacionada para os quatro possíveis lados e
comparada também.

As precisões ficam registradas em uma lista que no fim exibe o valor máximo.
'''

# A função "flip" espelha a matriz. Nesta função cada linha é revertida e colocada em uma matriz
# que será retornada
def flip(mat, l):

    flip_mat = [] # Matriz para retorno

    # Inverte cada linha da matriz e coloca na matriz de retorno
    for i in range(l):

        flip_mat.append(list(reversed(mat[i])))
    
    return flip_mat # Retorna a matriz espelhada

# Esta função rotaciona a matriz no sentido horário. Ela é uma função recursiva, então o valor de "a" define
# Quantas vezes será feita uma rotação. Ex: a = 2 -> rotaciona duas vezes, deixando a matriz de ponta-cabeça.
def rot(mat, l, a = 1):

    # Caso nenhuma rotação seja especificada retorna a própria matriz
    if a == 0:

        return mat

    rot_mat = [] # Matriz para retorno

    # Adiciona cada coluna da matriz original em linhas da nova matriz. O primeiro elemento da nova linha
    # será o último elemento da coluna
    for i in range(l):

        rot_mat.append([])

        for j in range(l):

            rot_mat[i].append(mat[l - j - 1][i])
    
    a -= 1 # Decrementa o a

    if a <= 0: # Caso as rotações terminaram

        return rot_mat # Retorna a nova matriz
    else: # Caso contrário

        return rot(rot_mat, l, a) # Chama a função recursivamente para mais uma rotação

# Esta função compara a diferença de cada elemento e calcula a precisão entre as matrizes
def comp_mat(mat_a, mat_b, l):

    p = 0 # Variável para a quantidade de elementos que satisfazem os critérios

    # Para cada elemento verifica se a diferença entre eles é menor ou igual a 100
    # Caso seja incrementa a quantidade de elementos precisos.
    for i in range(l):

        for j in range(l):

            if abs(mat_a[i][j] - mat_b[i][j]) <= 100:

                p += 1
    
    return (p * 100.0) / l ** 2.0 # Retorna o valor percentual da precisão

while True: # Loop para cada caso

    l = int(input()) # Entrada de l

    # Condição de saída
    if l == 0:
        break

    p_mat = [] # Matriz padrão
    t_mat = [] # Matriz de testes

    # Loop para a entrada da matriz padrão
    for _ in range(l):

        p_mat.append(list(map(int, input().split())))
    
    # Loop para a entrada da matriz de testes
    for _ in range(l):

        t_mat.append(list(map(int, input().split())))

    p_lst = [] # Lista de precisões

    for i in range(4): # Loop para cada rotação

        rot_mat = rot(t_mat, l, i) # Matriz rotacionada

        p_lst.append(comp_mat(p_mat, rot_mat, l)) # Adiciona a precisão na lista de precisões
    
    flip_mat = flip(t_mat, l) # Matriz espelhada

    for i in range(4): # Loop para cada rotação espelhada

        rot_mat = rot(flip_mat, l, i) # Matriz espelhada rotacionada

        p_lst.append(comp_mat(p_mat, rot_mat, l)) # Adiciona a precisão na lista de precisões
    
    print("{0:.2f}".format(max(p_lst))) # Exibe o resultado