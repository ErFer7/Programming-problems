"""
Conformity.
"""

while True:
    students = int(input())

    if students == 0:
        break

    combinations = {}

    for _ in range(students):
        courses = tuple(sorted(input().split()))

        if courses in combinations:
            combinations[courses] += 1
        else:
            combinations[courses] = 1

    most_popular = max(combinations.values())
    prizes = 0

    for combination in combinations.values():
        if combination == most_popular:
            prizes += most_popular

    print(prizes)
