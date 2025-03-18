"""
Dates.
"""

from datetime import datetime, timedelta

test_count = int(input())

for i in range(test_count):
    date = datetime.strptime(input(), '%Y-%B-%d')
    days = int(input())

    date += timedelta(days)

    print(f'Case {i + 1}: {date.strftime("%Y-%B-%d")}')
