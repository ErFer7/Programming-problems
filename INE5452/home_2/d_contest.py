"""
Contest Scoreboard.
"""

test_count = int(input())
input()

for i in range(test_count):
    contestants = {}

    while True:
        try:
            line = input()
        except EOFError:
            break

        if line == '':
            break

        contestant, problem, time, status = line.split()
        contestant = int(contestant)

        if contestant not in contestants:
            contestants[contestant] = [{}, 0, 0]  # Problemas, problemas resolvidos, penalidade

        if problem not in contestants[contestant][0]:
            contestants[contestant][0][problem] = [False, 0]  # Resolvido, submissões incorretas

        if status == 'C':
            if not contestants[contestant][0][problem][0]:
                contestants[contestant][0][problem][0] = True
                contestants[contestant][1] += 1
                contestants[contestant][2] += int(time) + 20 * contestants[contestant][0][problem][1]
        elif status == 'I':
            contestants[contestant][0][problem][1] += 1

    scoreboard = sorted(contestants.items(), key=lambda x: (-x[1][1], x[1][2], x[0]))

    for contestant, (_, problems_solved, penalty) in scoreboard:
        print(contestant, problems_solved, penalty)

    if i < test_count - 1:
        print()
