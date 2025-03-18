# -*- coding: utf-8 -*-

a = list(map(int, input().split()))
b = list(map(int, input().split()))

comp = True

for i in range(5):

    if a[i] == b[i]:

        comp = False

if comp:

    print("Y")
else:

    print("N")