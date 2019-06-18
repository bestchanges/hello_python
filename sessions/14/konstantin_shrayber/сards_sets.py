import datetime
import math
from collections import deque

base_deck = [u'2\u2660', u'3\u2660', u'4\u2660', u'5\u2660', u'6\u2660', u'7\u2660', u'8\u2660', u'9\u2660', u'10\u2660', u'J\u2660', u'Q\u2660', u'K\u2660', u'A\u2660',
             u'2\u2663', u'3\u2663', u'4\u2663', u'5\u2663', u'6\u2663', u'7\u2663', u'8\u2663', u'9\u2663', u'10\u2663', u'J\u2663', u'Q\u2663', u'K\u2663', u'A\u2663',
             u'2\u2666', u'3\u2666', u'4\u2666', u'5\u2666', u'6\u2666', u'7\u2666', u'8\u2666', u'9\u2666', u'10\u2666', u'J\u2666', u'Q\u2666', u'K\u2666', u'A\u2666',
             u'2\u2665', u'3\u2665', u'4\u2665', u'5\u2665', u'6\u2665', u'7\u2665', u'8\u2665', u'9\u2665', u'10\u2665', u'J\u2665', u'Q\u2665', u'K\u2665', u'A\u2665']


def create_deck() -> deque:
    x = base_deck.copy()
    shuffled = deque()

    while len(x) > 0:
        index = math.floor(int(str(datetime.datetime.now().time())[-4:-1]) * len(x) / 999)

        if index % 2 == 0:
            shuffled.append(x.pop(index))
        else:
            shuffled.appendleft(x.pop(index))

        if index * 2 < len(x):
            shuffled.rotate(index+10)
        else:
            shuffled.rotate(-index-5)

    return shuffled


def give_cards(amount: int, deck: deque) -> set:
    hand = set()

    for i in range(amount):
        hand.add(deck.popleft())

    return hand


deck1 = create_deck()
deck2 = create_deck()

hand1 = give_cards(10, deck1)
hand2 = give_cards(10, deck2)

print("initial hands")
print(hand1, hand2)

print("common cards")
print(hand1.intersection(hand2))

print("cards from hand1 not present in hand2")
print(hand1.difference(hand2))

print("cards different in both hands")
print(hand1.symmetric_difference(hand2))

for card in hand1.difference(hand2):
    deck2.remove(card)

print("deck2 after cleaning of cards from hand1")
print(deck2)
