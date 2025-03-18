"""
Rock-Paper-Scissors Tournament.
"""

tested_before = False

while True:
    values = input()

    if values == '0':
        break

    if tested_before:
        print()

    players, game_count = tuple(map(int, values.split()))
    ratios = {player: [0, 0] for player in range(1, players + 1)}

    for _ in range(game_count * players * (players - 1) // 2):
        player_a, move_a, player_b, move_b = input().split()
        player_a = int(player_a)
        player_b = int(player_b)
        winner = 0
        loser = 0

        # Regular if-else because this will run on Python 3.5
        if move_a == 'rock':
            if move_b == 'paper':
                winner = player_b
                loser = player_a
            elif move_b == 'scissors':
                winner = player_a
                loser = player_b
        elif move_a == 'paper':
            if move_b == 'rock':
                winner = player_a
                loser = player_b
            elif move_b == 'scissors':
                winner = player_b
                loser = player_a
        elif move_a == 'scissors':
            if move_b == 'rock':
                winner = player_b
                loser = player_a
            elif move_b == 'paper':
                winner = player_a
                loser = player_b

        if winner != 0:
            ratios[winner][0] += 1
            ratios[loser][1] += 1

    for player in range(1, players + 1):
        ratio_sum = sum(ratios[player])

        if ratio_sum == 0:
            print('-')
        else:
            print(f'{ratios[player][0] / ratio_sum:.3f}')

    tested_before = True
