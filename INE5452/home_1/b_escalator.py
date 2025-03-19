"""
Escalator.
"""

test_count = int(input())

entry_events = [tuple(map(int, input().split())) for _ in range(test_count)]
waiting = False
total_time = 0
escalator_direction = None

while len(entry_events) > 0 or waiting:
    if waiting:
        if len(entry_events) > 0 and entry_events[0][0] > total_time:
            waiting = False
            entry_events.insert(0, (total_time, (1, 0)[escalator_direction]))
            escalator_direction = None
        elif len(entry_events) == 0:
            waiting = False
            entry_events.insert(0, (total_time, (1, 0)[escalator_direction]))
            escalator_direction = None

    timestamp, direction = entry_events.pop(0)

    if direction == escalator_direction or escalator_direction is None:
        escalator_direction = direction
        total_time = timestamp + 10
    else:
        waiting = True


print(total_time)
