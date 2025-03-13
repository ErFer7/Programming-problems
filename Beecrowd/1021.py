# -*- coding: utf-8 -*-

valueInput = float(input())
value = int(valueInput * 100.0)

notes_100 = value // 10000
value -= 10000 * notes_100

notes_50 = value // 5000
value -= 5000 * notes_50

notes_20 = value // 2000
value -= 2000 * notes_20

notes_10 = value // 1000
value -= 1000 * notes_10

notes_5 = value // 500
value -= 500 * notes_5

notes_2 = value // 200
value -= 200 * notes_2

coin_1 = value // 100
value -= 100 * coin_1

coin_050 = value // 50
value -= 50 * coin_050

coin_025 = value // 25
value -= 25 * coin_025

coin_010 = value // 10
value -= 10 * coin_010

coin_005 = value // 5
value -= 5 * coin_005

coin_001 = value // 1

print("NOTAS:")
print("%d nota(s) de R$ 100.00" % notes_100)
print("%d nota(s) de R$ 50.00" % notes_50)
print("%d nota(s) de R$ 20.00" % notes_20)
print("%d nota(s) de R$ 10.00" % notes_10)
print("%d nota(s) de R$ 5.00" % notes_5)
print("%d nota(s) de R$ 2.00" % notes_2)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % coin_1)
print("%d moeda(s) de R$ 0.50" % coin_050)
print("%d moeda(s) de R$ 0.25" % coin_025)
print("%d moeda(s) de R$ 0.10" % coin_010)
print("%d moeda(s) de R$ 0.05" % coin_005)
print("%d moeda(s) de R$ 0.01" % coin_001)