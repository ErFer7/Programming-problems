"""
All all.
"""

from bisect import insort

while True:
    number_count = int(input())

    if number_count == 0:
        break

    numbers = sorted(map(int, input().split()))
    total_cost = 0
    result = 0

    while True:
        result = numbers.pop(0) + numbers.pop(0)
        total_cost += result

        if len(numbers) == 0:
            break

        insort(numbers, result)

    print(total_cost)