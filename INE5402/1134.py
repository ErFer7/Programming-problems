# -*- coding: utf-8 -*-

alcohol, gasoline, diesel = (0, 0, 0)

while True:

    fuel = int(input())

    if fuel == 1:

        alcohol += 1
    elif fuel == 2:

        gasoline += 1
    elif fuel == 3:

        diesel += 1
    elif fuel == 4:

        print("MUITO OBRIGADO")
        print("Alcool: %d" % alcohol)
        print("Gasolina: %d" % gasoline)
        print("Diesel: %d" % diesel)
        break