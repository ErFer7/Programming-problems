"""
What is the Card?
"""


def card_value(card):
    """
    Calcula o valor da carta.
    """

    first = card[0]

    if first.isnumeric():
        return int(first)

    return 10


test_count = int(input())

for i in range(test_count):
    cards = input().split()

    top_cards = cards[27:]  # Top 25
    cards = cards[:27]

    y_index = 0

    for _ in range(3):
        top_card = cards.pop()
        value = card_value(top_card)
        y_index += value
        slice_value = 10 - value

        if slice_value > 0:
            cards = cards[:-(10 - value)]

    cards += top_cards

    print(f'Case {i + 1}: {cards[y_index - 1]}')
