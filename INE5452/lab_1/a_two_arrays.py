"""
Milya and Two Arrays.
"""

test_count = int(input())

for test in range(test_count):
    arrays_length = int(input())
    distinct_count_a = len(set(tuple(map(int, input().split()))))
    distinct_count_b = len(set(tuple(map(int, input().split()))))

    if distinct_count_a + distinct_count_b > 3:
        print('YES')
        continue

    print('NO')
