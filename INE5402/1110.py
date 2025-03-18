# -*- coding: utf-8 -*-

'''
Jogando Cartas Fora
'''

while True:

    card_count = int(input())

    if card_count == 0:
        break

    cards = list(range(card_count, 0, -1))
    discarted_cards = []

    while len(cards) >= 2:

        discarted_cards.append(cards.pop())
        cards.insert(0, cards.pop())

    print("Discarded cards: " + ", ".join(str(n) for n in discarted_cards))
    print(f"Remaining card: {cards[0]}")
