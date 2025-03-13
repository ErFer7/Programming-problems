# -*- coding: utf-8 -*-

n = int(input())
stopTime = 0
totalTime = 0

for i in range(n):

    t = int(input())

    if t < stopTime:

        totalTime += (t + 10) - stopTime
        stopTime = t + 10
    else:
            
        totalTime += 10
        stopTime = t + 10

print(totalTime)