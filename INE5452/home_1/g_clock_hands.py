"""
Clock Hands.
"""

while True:
    hours, minutes = tuple(map(int, input().split(':')))

    if hours == 0 and minutes == 0:
        break

    if hours == 12:
        hours = 0

    angle = hours * 30 - minutes * 5.5

    if angle < 0:
        angle = -angle

    if angle > 180:
        angle = 360 - angle

    print(f'{angle:.3f}')
