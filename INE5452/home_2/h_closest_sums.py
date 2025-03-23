"""
Closest Sums.
"""

from bisect import insort

test_case = 1

while True:
    number_count = int(input())

    if number_count == 0:
        break

    numbers = []

    for _ in range(number_count):
        number = int(input())

        insort(numbers, number)

    query_count = int(input())

    cache = {}

    print('Case {}:'.format(test_case))

    for _ in range(query_count):
        query = int(input())

        closest_sum = cache.get(query, -999)

        if closest_sum == -999:
            left = 0
            right = len(numbers) - 1

            if query <= numbers[left] + numbers[left + 1]:
                closest_sum = numbers[left] + numbers[left + 1]
            elif query >= numbers[right - 1] + numbers[right]:
                closest_sum = numbers[right - 1] + numbers[right]
            else:
                while left < right and left >= 0 and right < len(numbers):
                    new_closest_sum = numbers[left] + numbers[right]

                    if new_closest_sum == query:
                        closest_sum = new_closest_sum
                        break

                    if closest_sum == -999 or abs(query - new_closest_sum) < abs(query - closest_sum) or (
                            abs(query - new_closest_sum) == abs(query - closest_sum) and new_closest_sum < closest_sum):
                        closest_sum = new_closest_sum

                    if new_closest_sum < query:
                        left += 1
                    else:
                        right -= 1

        cache[query] = closest_sum

        print('Closest sum to {} is {}.'.format(query, closest_sum))

    test_case += 1
