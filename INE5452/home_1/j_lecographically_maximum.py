"""
Lecographically Maximum.
"""

import pyinstrument

from math import log2


with pyinstrument.profile():
    test_count = int(input())
    numbers = tuple(map(int, input().split()))
    position_counter = [0] * 30
    sorted_numbers = [0]

    for number in numbers:
        for bit in range(int(log2(number)) + 1):
            position_counter[bit] += (number >> bit) & 1

with pyinstrument.profile():
    last_bit = 29
    next_last_bit = 0

    for _ in range(test_count):
        new_number = 0

        for bit, digit in enumerate(position_counter):
            if bit > last_bit:
                break

            if digit > 0:
                new_number |= 1 << bit
                position_counter[bit] -= 1
                next_last_bit = bit

        last_bit = next_last_bit

        sorted_numbers.append(new_number)

    print(*sorted_numbers)
