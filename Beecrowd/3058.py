# -*- coding: utf-8 -*-

# Número de mercados.
n = int(input())

# A ideia é comparar a rentabilidade de cada mercado em um loop. A rentabilidade será dada pela massa em gramas
# dividida pelo preço, caso a rentabilidade seja maior que a contida na variável rMax o novo valor de rMax 
# será aquela nova rentabilidade. Por causa disso a variável rMax foi declarada com o valor -1, assim o primeiro 
# valor sempre é registrado na variável pois este sempre será maior que rMax.

# Com a comparação da rentabilidade o preço também será calculado e registrado. Toda vez que o valor de rMax for 
# alterado com outro mercado o valor da variável pMin será registrado como o preço para comprar 1 kg de carne
# naquele mercado.

# Variável da rentabilidade, declarada com -1 por causa da maneira que serão comparados os valores.
rMax = -1
# Variável de menor preço para comprar 1 kg de carne.
pMin = 0

# O loop a seguir irá ser executado para cada mercado.
for i in range(n):

    # A variável pg se refere a (preço, grama), neste caso foi obtido o input e separado em um vetor de 2 elementos.
    # Este vetor foi "mapeado" com a função map() aplicando a função float() aos 2 elementos e convertendo os mesmos
    # para float. Depois o mapa foi convertido em lista pela função list(), assim os valores podem ser acessados fácilmente
    pg = list(map(float, input().split()))

    # O valor da rentabilidade será a massa pg[1] dividida pelo preço pg[0].
    r = pg[1] / pg[0]

    # Compara se a rentabilidade é maior que a rentabilidade máxima registrada.
    if r > rMax:

        # Caso a condição for verdadeira registra a nova rentabilidade máxima.
        rMax = r
        # O novo menor preço é dado por 1000 dividido pela rentabilidade, pois a unidade da rentabilidade é g/B$
        # então 1000(g) / r(g/B$) resulta no preço em B$
        pMin = 1000 / r

# Escreve no console o menor preço para comprar 1 kg de carne com 2 casas decimais.
print("{:.2f}".format(pMin))