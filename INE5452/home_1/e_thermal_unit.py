"""
A Change in Thermal Unit.
"""

tests_count = int(input())

for i in range(tests_count):
    celsius_temperature, farenheit_increase = tuple(map(int, input().split()))

    print(f'Case {i + 1}: {celsius_temperature + farenheit_increase * 5 / 9:.2f}')
