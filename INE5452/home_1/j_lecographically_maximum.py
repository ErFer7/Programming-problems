"""
Lecographically Maximum.
"""

test_count = int(input())
numbers = tuple(map(int, input().split()))
position_counter = [0] * 30
sorted_numbers = [0] * test_count

for number in numbers:
    for bit in range(30):
        position_counter[bit] += (number >> bit) & 1

for bit, count in enumerate(position_counter):
    if count > 0:
        for i in range(count):
            sorted_numbers[i] |= 1 << bit

print(*sorted_numbers)
