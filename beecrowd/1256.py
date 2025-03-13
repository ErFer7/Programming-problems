# -*- coding: utf-8 -*-

'''
Tabelas Hash
'''

test_count = int(input())

for i in range(test_count):

    adress_count, key_count = map(int, input().split())
    keys = list(map(int, input().split()))

    hash_table = [[] for _ in range(adress_count)]

    for key in keys:
        hash_table[key % adress_count].append(key)

    for j in range(adress_count):

        final_arrow = " -> " if len(hash_table[j]) > 0 else ''
        print(f"{j} -> " + " -> ".join([str(key) for key in hash_table[j]]) + final_arrow + "\\")

    if i < test_count - 1:
        print()
