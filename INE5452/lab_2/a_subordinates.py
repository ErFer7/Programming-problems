"""
Subordinates.
"""

employee_count = int(input())
relationships = tuple(map(int, input().split()))

if employee_count == 1:
    print(0)
    exit()

tree = {i: [0, [], 0] for i in range(1, employee_count + 1)}  # employee: [boss, subordinate, subordinate_count]
visited = [employee for employee in range(1, employee_count + 1)]

for i, boss in enumerate(relationships):
    employee = i + 2
    tree[employee][0] = boss
    tree[boss][1].append(employee)

    try:
        visited.remove(boss)
    except ValueError:
        pass


while len(visited) > 0:
    current_employee = visited.pop(0)

    boss = tree[current_employee][0]

    if boss == 0:
        break

    tree[boss][2] += tree[current_employee][2] + 1

    if boss not in visited:
        visited.append(boss)

for employee, (_, _,subordinate_count) in tree.items():
    print(subordinate_count, end=(' ' if employee < len(tree) else ''))

print()
