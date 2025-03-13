# -*- coding: utf-8 -*-

'''
Para resolver este problema são seguidos os seguintes passos:

1. É feita a leitura da matriz e para cada linha em que há prateleiras os seus inícios e fins são colocados
em uma lista. Isso significa que se uma prateleira começa em 2 e termina e 5 ela será registrada como [2, 5].
No fim dessa etapa a leitura está completa e há uma lista com as "coordenadas" das plataformas para cada linha.

2. É localizada a posição inicial da goteira e coloca ela em uma lista usada para simular as colunas de água.

3. São usadas duas listas nessa parte, uma delas armazena as posições já processadas e a outra armazena as que
ainda devem ser processadas. Cada posição na lista a ser processada é analisada da seguinte forma:

    3.1 Caso não haja nenhum obstáculo reduz a altura da gota (simulando a água caindo) e marca a posição passada
    na lista de posições processadas. Quando há um obstáculo ou o fim da matriz esse loop para.

    3.2 O próximo caso verifica se a gota está em contato com alguma prateleira, caso esteja todas as posições em 
    cima da prateleira são preenchidas na lista de posições processadas. Nos dois cantos da prateleira são criadas 
    as novas posições das gotas na lista de processamento.

    3.3 No fim a gota atual é deletada para que as próximas sejam simuladas.

4. No final do processo anterior o resultado é uma matriz em que cada linha contém uma série de números que
representam as posições na matriz origiral que devem ter água. Com isso é feita a criação da matriz de resultado
em que cada linha recebe os caracteres correspondentes.

5. Exibe a matriz resultante.
'''

n, m = map(int, input().split()) # Entrada de n e m

c = [] # Matriz de entrada
prat_mat = [] # Matriz de prateleiras
a_lst = [] # Lista de gotas que devem ser processadas
ap_mat = [] # Matriz com as posições das gotas já processadas

for i in range(n): # Loop para cada linha de entrada

    ln = input() # Entrada da linha

    c.append(ln) # Adiciona a linha na matriz de entrada

    ap_mat.append([]) # Cria uma nova linha na matriz de gotas a serem processadas

    if i % 2 != 0: # Caso a linha seja impar

        prat_mat.append([]) # Cria uma nova linha na matriz de prateleiras

        in_prat = False # Variável para definir se uma prateleira iniciou
        prat_count = 0 # Contagem de prateleiras

        for j in range(m): # Para cada coluna nesta linha

            if ln[j] == '#' and not in_prat: # Se uma prateleira está iniciando

                in_prat = True # Define que uma prateleira iniciou a partir desta posição
                prat_mat[i].append([j]) # Adiciona a posição de início
                prat_count += 1 # Incrementa a contagem
            elif ln[j] == '.' and in_prat: # Caso uma prateleira tenha acabado

                in_prat = False # Define que uma prateleira terminou na posição anterior
                prat_mat[i][prat_count - 1].append(j - 1) # Adiciona a posição de fim
    else:

        prat_mat.append(None) # Adiciona um valor nulo já que nas linhas pares não há prateleiras

for i in range(m): # Loop para encontra a posição da primeira gota

    if c[0][i] == 'o': # Caso tenha uma gota nesta coluna

        a_lst.append([0, i]) # Adiciona a sua posição na lista para processamento
        break

while len(a_lst) > 0: # Enquanto ouverem gotas não processadas

    while a_lst[0][0] < n: # Caso a gota não tenha chegado ao fim da matriz

        if a_lst[0][1] not in ap_mat[a_lst[0][0]]: # Caso não haja uma gota nesta posição
            
            ap_mat[a_lst[0][0]].append(a_lst[0][1]) # Adiciona a posiçõa na lista de gotas processadas

        if a_lst[0][0] < n - 1: # Caso a posição atual não seja a penúltima da matriz

            # Se a posição abaixo tem uma plataforma ou uma gota
            if c[a_lst[0][0] + 1][a_lst[0][1]] == '#' or a_lst[0][1] in ap_mat[a_lst[0][0] + 1]:

                break # Quebra o loop

        a_lst[0][0] += 1 # Incrementa a posição vertical (desce a linha da gota)

    # Caso a linha seja par e a posição atual não seja a penúltima da matriz
    # Neste caso existe a possibilidade de ter uma plataforma abaixo
    if a_lst[0][0] % 2 == 0 and a_lst[0][0] < n - 1:

        for p in prat_mat[a_lst[0][0] + 1]: # Para cada plataforma na linha abaixo

            if a_lst[0][1] >= p[0] and a_lst[0][1] <= p[1]: # Se a gota está em cima da plataforma

                for i in range(p[0], p[1] + 1): # Para cada posição acima da posição que a plataforma ocupa

                    if i not in ap_mat[a_lst[0][0]]: # Caso não haja uma gota naquela posição

                        ap_mat[a_lst[0][0]].append(i) # Adiciona uma gota na lista de gotas processadas

                # Adiciona uma nova gota a ser processada na esquerda da plataforma
                a_lst.append([a_lst[0][0], p[0] - 1])

                # Adiciona uma nova gota a ser processada na direita da plataforma
                a_lst.append([a_lst[0][0], p[1] + 1])
    
    a_lst.remove(a_lst[0]) # Remove a gota atual que já foi processada

for i in range(n): # Para cada linha

    ln = "" # Cria um novo string para a linha

    for j in range(m): # Para cada coluna

        if j in ap_mat[i]: # Caso a posição tenha uma gota

            ln += 'o' # Adiciona a gota no string da linha
        else: # Caso contrário

            ln += c[i][j] # Adiciona o caractere original no string da linha
        
    print(*ln, sep = '') # Exibe a linha resultante
