# -*- coding: utf-8 -*-

highestNumber = -1
highestNumberPosition = -1

for i in range(100):

    number = int(input())

    if number > highestNumber:

        highestNumber = number
        highestNumberPosition = i + 1

print(highestNumber)
print(highestNumberPosition)