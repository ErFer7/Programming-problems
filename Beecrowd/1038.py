# -*- coding: utf-8 -*-

order = input().split()

prices = [4.0, 4.5, 5.0, 2.0, 1.5]

print("Total: R$ %.2f" % (prices[int(order[0]) - 1] * int(order[1])))