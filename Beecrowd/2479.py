# -*- coding: utf-8 -*-

def func(comp_list, cr_list):

    ord_list = sorted(cr_list)

    return comp_list.count('+'), comp_list.count('-'), ord_list

n = int(input())

comp_list = []
cr_list = []

for _ in range(n):

    comp, cr = map(str, input().split())

    comp_list.append(comp)
    cr_list.append(cr)

p_comp, n_comp, cr_ord = func(comp_list, cr_list)

for c in cr_ord:

    print(c)
    
print("Se comportaram: {0} | Nao se comportaram: {1}".format(p_comp, n_comp))