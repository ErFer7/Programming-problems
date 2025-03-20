"""
Throwing cards away I.
"""

while True:
    card_n = int(input())

    if card_n == 0:
        break

    cards = [str(card) for card in range(1, card_n + 1)]
    discarded = []

    while len(cards) >= 2:
        discarded.append(cards.pop(0))
        new_top = cards.pop(0)
        cards.append(new_top)

    print('Discarded cards:' + (' ' if card_n > 1 else '') + ', '.join(discarded))
    print('Remaining card: ' + cards[0])
