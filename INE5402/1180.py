# -*- coding: utf-8 -*-

n = int(input())

nCLst = list(map(int, input().split()))[:n]

print("Menor valor: %d" % min(nCLst))
print("Posicao: %d" % nCLst.index(min(nCLst)))