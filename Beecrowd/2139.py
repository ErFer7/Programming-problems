# -*- coding: utf-8 -*-

import datetime

while True:

    try:

        case = input().split()
        
        month = int(case[0])
        day = int(case[1])

        caseDate = datetime.date(2016, month, day)
        christmas = datetime.date(2016, 12, 25)

        delta = christmas - caseDate
        if delta.days > 1:

            print("Faltam %d dias para o natal!" % delta.days)
        elif delta.days == 1:

            print("E vespera de natal!")
        elif delta.days == 0:

            print("E natal!")
        else:

            print("Ja passou!")

    except EOFError:
        break