# -*- coding: utf-8 -*-

import datetime

a = list(map(int, input().split()))
b = list(map(int, input().split()))

initialDate = datetime.date(2019, a[1], a[0])
finalDate = datetime.date(2019, b[1], b[0])

delta = finalDate - initialDate

print(delta.days)