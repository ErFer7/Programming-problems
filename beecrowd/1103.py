# -*- coding: utf-8 -*-

'''
Alarme Despertador
'''

while True:

    h1, m1, h2, m2 = map(int, input().split())

    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break

    current_minutes = h1 * 60 + m1
    alarm_minutes = h2 * 60 + m2

    if current_minutes < alarm_minutes:
        print(alarm_minutes - current_minutes)
    else:
        print(1440 - (current_minutes - alarm_minutes))
