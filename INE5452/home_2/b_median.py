"""
What is the Median?
"""

from bisect import insort

numbers = []

while True:
    try:
        insort(numbers, int(input()))
        length = len(numbers)
        half = length // 2

        if length % 2 != 0:
            print(numbers[half])
        else:
            print((numbers[half - 1] + numbers[half]) // 2)
    except EOFError:
        break
