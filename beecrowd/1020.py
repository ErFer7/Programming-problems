# -*- coding: utf-8 -*-

timeInDays = int(input())

years = int(timeInDays / 365)
months = int((timeInDays % 365) / 30)
days = int((timeInDays % 365) % 30)

print("%d ano(s)" % years)
print("%d mes(es)" % months)
print("%d dia(s)" % days)