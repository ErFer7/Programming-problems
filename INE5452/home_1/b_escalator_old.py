"""
Escalator.
"""

test_count = int(input())

total_time = 0
escalator_direction = None
waiting_direction = None

for _ in range(test_count):
    time, direction = tuple(map(int, input().split()))

    if time > total_time:
        if waiting_direction is not None:
            total_time += 10
            time = total_time

        escalator_direction = None
        waiting_direction = None

    if escalator_direction is None:
        escalator_direction = direction

    if direction == escalator_direction:
        increased_time = time + 10

        if increased_time > total_time:
            total_time = increased_time
    else:
        waiting_direction = direction

if waiting_direction is not None:
    total_time += 10

print(total_time)
