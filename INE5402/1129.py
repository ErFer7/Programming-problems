# -*- coding: utf-8 -*-

'''
Leitura Ótica
'''

while True:

    nQuestions = int(input())
    choices = ["A", "B", "C", "D", "E"]

    if nQuestions == 0:
        break

    for i in range(nQuestions):

        marked = -1
        valid = False

        nLst = list(map(int, input().split()))

        for j in nLst:

            if j <= 127:

                if marked == -1:

                    marked = nLst.index(j)
                    valid = True
                else:

                    valid = False

        if valid:

            print(choices[marked])
        else:

            print("*")
