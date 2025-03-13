# -*- coding: utf-8 -*-

# NOTA: Não pensei em uma implementação que não usasse vetores.

# O problema pede que sejam calculadas as medias móveis das temperaturas. 
# O processo para calcular a média móvel é subtrair o somatório de média mais antigo e adicionar o novo a cada
# iteração do loop, assim temos que a média móvel naquele ponto é (novo valor - valor mais antigo) / intervalo
# O valor novo é obtido a cada iteração do loop enquanto o valor mais antigo é registrado em uma lista que tem
# o seu primeiro elemento acessado e deletado a cada iteração. Com a média calculada é possível adicioná-la a 
# lista.

# Ainda existe o cálculo da média antes da remoção do elemento mais antigo, que no caso se dá pelo somatório das
# operações (temperatura / intervalo).
# É por causa dessa condição inicial que o loop possui o condicional que checa se a temperatura nova em questão 
# já deve ser calculada para a próxima média. Este também é o motivo da média ser adicionada na lista de médias 
# antes de ser calculada pelo método (novo valor - valor mais antigo) / intervalo pois é necessário adicionar a 
# primeira média antes de continuar o cálculo.

# Ainda existem mais duas condições importantes. No final do cálculo da média móvel é checado se a temperatura é
# a última em questão, caso seja a média é adicionada na lista de médias. Caso esta condição não existisse a última
# média seria perdida.
# A outra condição é de que n é igual a m, neste caso a média será calculada como uma média normal.

# Ao final dessas operações são usadas as funções min() e max() na lista de médias, assim obtendo a menor e maior
# média.

# Variável para a contagem.
count = 0

# Loop que processa cada caso de testes.
while True:

    # Incrementa o contador em 1.
    count += 1

    # Lista de temperaturas e médias de temperaturas
    tLst = []
    mTLst = []

    # Veriável da média da temperatura
    mT = 0.0

    # Input de n e m. O input é separado em um vetor de 2 elementos e depois mapeado e convertido para int.
    n, m = map(int, input().split())

    # Intervalo em float
    inter = float(m)

    # Condição de saída, quebra o loop caso n e m sejam 0.
    if n == 0 and m == 0:
        break

    # Loop que processa cada input de temperatura.
    for i in range(n):

        # Armazena o input de uma temperatura.
        t = float(input())
        
        # Adiciona a temperatura na lista
        tLst.append(t)

        # Condição aonde são calculas as médias móveis
        if i > m - 1:
            
            # Adiciona a temperatura média calculada anteriormente na lista
            mTLst.append(mT)
            # Calcula a temperatura média
            mT += (t - tLst[0]) / inter
            # Deleta o primeiro item da lista de temperaturas
            del tLst[0]

            # Caso seja a última iteração do loop a média da temperatura é adicionada
            if i == n - 1:
                mTLst.append(mT)
        # Condição de antes do primeiro cálculo da média móvel
        else:

            # Calcula a teperatura média
            mT += t / inter

            # Condição para o caso em que só existe uma média a ser calculada
            if n == m and i == n - 1:

                # Adiciona a temperatura média na lista
                mTLst.append(mT)
        
    # Escreve no console "Teste n".
    print("Teste {0}".format(count))
    # Escreve no console a menor e maior média truncada. (Neste caso convertida para int).
    # Detalhe, os valores são arredondados na 12° casa decimal por causa dos erros de precisão que estavam
    # causando problemas na avaliação do URI.
    print("{0} {1}\n".format(int(round(min(mTLst), 12)), int(round(max(mTLst), 12))))