import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*4

presentacion= input("")
def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand
    

print(deal(deck))

