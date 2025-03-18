# -*- coding: utf-8 -*-

# Código do professor

n = int(input())

ln = input().split()

while n > 1:

    mat = []

    for i in range(n - 1):

        if ln[i] == ln[i + 1]:

            mat.append('1')
        else:

            mat.append('-1')
            
    ln = mat
    n -= 1
    
if ln[0] == '1':

    print("preta")
else:

    print("branca")