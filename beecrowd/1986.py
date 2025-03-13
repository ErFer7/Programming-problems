# -*- coding: utf-8 -*-

n = int(input())

hexM = "".join(input().split())

m = bytes.fromhex(hexM).decode('ascii')

print(m)