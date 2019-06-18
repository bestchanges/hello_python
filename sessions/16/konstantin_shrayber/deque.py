import datetime
import math
from collections import deque
from random import randint

base_deck = [u'2\u2660', u'3\u2660', u'4\u2660', u'5\u2660', u'6\u2660', u'7\u2660', u'8\u2660', u'9\u2660', u'10\u2660', u'J\u2660', u'Q\u2660', u'K\u2660', u'A\u2660',
             u'2\u2663', u'3\u2663', u'4\u2663', u'5\u2663', u'6\u2663', u'7\u2663', u'8\u2663', u'9\u2663', u'10\u2663', u'J\u2663', u'Q\u2663', u'K\u2663', u'A\u2663',
             u'2\u2666', u'3\u2666', u'4\u2666', u'5\u2666', u'6\u2666', u'7\u2666', u'8\u2666', u'9\u2666', u'10\u2666', u'J\u2666', u'Q\u2666', u'K\u2666', u'A\u2666',
             u'2\u2665', u'3\u2665', u'4\u2665', u'5\u2665', u'6\u2665', u'7\u2665', u'8\u2665', u'9\u2665', u'10\u2665', u'J\u2665', u'Q\u2665', u'K\u2665', u'A\u2665']


def cards_shuffle(deck_to_shuffle) -> deque:
    x = list(deck_to_shuffle)
    shuffled = deque()

    while len(x) > 0:
        index = math.floor(int(str(datetime.datetime.now().time())[-4:-1]) * len(x) / 999)

        if index % 2 == 0:
            shuffled.append(x.pop(index))
        else:
            shuffled.appendleft(x.pop(index))

        if index * 2 < len(x):
            shuffled.rotate(index + 10)
        else:
            shuffled.rotate(-index - 5)

    return shuffled


cards = deque(base_deck)
print('initial cards', cards)


cards = cards_shuffle(cards)
print('shuffled cards', cards)

cards.rotate(randint(0, 52))
print('rotated cards', cards)

black_deck = deque()
red_deck = deque()
for i in range(len(cards)):
    card = cards.pop()
    if u'\u2660' in card or u'\u2663' in card:
        black_deck.append(card)
    else:
        red_deck.append(card)
print('current cards', cards)
print('black cards', black_deck)
print('red cards', red_deck)

cards.extend(black_deck)
cards.extend(red_deck)
print('current cards', cards)

cards = cards_shuffle(cards)
print('shuffled cards again', cards)

cards.append(cards.popleft())
print('card from left moved to right', cards)
