"""
Playing 23.
"""


def get_points(card: int) -> int:
    """
    Obtém os pontos de uma carta.
    """

    if card > 10:
        return 10

    return card


rounds_played = int(input())

johns_cards = tuple(map(int, input().split()))
marys_cards = tuple(map(int, input().split()))
common_cards = tuple(map(int, input().split()))
card_number_count = {card: 4 for card in range(1, 14)}

for card in johns_cards + marys_cards + common_cards:
    card_number_count[card] -= 1

johns_points = sum(map(get_points, johns_cards + common_cards))
marys_points = sum(map(get_points, marys_cards + common_cards))

lowest_card_value = -1

marys_diff = 23 - marys_points
johns_diff = 24 - johns_points

lowest_possible_card = marys_diff if marys_diff < johns_diff else johns_diff

for card in range(lowest_possible_card, 14):
    if card_number_count[card] > 0:
        card_value = get_points(card)
        marys_new_points = marys_points + card_value

        if marys_new_points > 23:
            break

        if marys_new_points == 23:
            lowest_card_value = card_value
            break

        if johns_points + card_value > 23:
            lowest_card_value = card_value
            break

print(get_points(lowest_card_value))
