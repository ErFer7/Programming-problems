# -*- coding: utf-8 -*-

m = input().split()

for i in range(len(m)):

    for j in range(len(m[i])):

        m[i] = m[i][0:j] + m[i][j + 1:]

    
print(" ".join(m))