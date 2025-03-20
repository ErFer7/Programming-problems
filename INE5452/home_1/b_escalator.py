"""
Escalator.
"""

test_count = int(input())
entry_events = [tuple(map(int, input().split())) for _ in range(test_count)]
escalator_direction = None
total_time = 0
next_stop = 0
waiting = False

while len(entry_events) > 0 or waiting:
    if len(entry_events) > 0:
        if next_stop < entry_events[0][0]:
            if waiting:
                entry_events.insert(0, (next_stop, (1, 0)[escalator_direction]))
            escalator_direction = None
            waiting = False
    elif waiting:
        entry_events.insert(0, (next_stop, (1, 0)[escalator_direction]))
        escalator_direction = None
        waiting = False

    timestamp, direction = entry_events.pop(0)

    if direction == escalator_direction or escalator_direction is None:
        escalator_direction = direction
        next_stop = max(timestamp + 10, next_stop)
    else:
        waiting = True

print(next_stop)
