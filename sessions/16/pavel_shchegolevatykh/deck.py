import uuid
from collections import namedtuple, deque
from itertools import islice
from random import randrange

Card = namedtuple('Card', ['value', 'suit', 'color'])


def ranks(): return ['Ace', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']


def suits(): return ['\u2663', '\u2666', '\u2665', '\u2660']


def shuffle(deck): return deque(sorted(deck, key=lambda x: uuid.uuid4()))


def create_deck(): return deque([Card(rank, suit, 'Red' if suit in ('\u2665', '\u2666') else 'Black') for rank in ranks() for suit in suits()])


def get_reds(deck): return deque([card for card in deck if card.color == "Red"])


def get_blacks(deck): return deque([card for card in deck if card.color == "Black"])


card_deck = create_deck()
print(f'Deck in default order: {card_deck}')

shuffled_deck = shuffle(card_deck)
print(f'Shuffled deck: {shuffled_deck}')

cut_point = randrange(len(shuffled_deck))
cut1 = deque(islice(shuffled_deck, 0, cut_point))  # array slicing [:cut_point] or [cut_point:] does not work on deque
cut2 = deque(islice(shuffled_deck, cut_point, len(shuffled_deck)))
print(f'First half: {cut1}')
print(f'Second half: {cut2}')

red_cards = get_reds(shuffled_deck)
black_cards = get_blacks(shuffled_deck)

print(f'Red cards: {red_cards}')
print(f'Black cards: {black_cards}')

combined_cards = red_cards + black_cards
print(f'Combined cards: {combined_cards}')

shuffled_deck = shuffle(combined_cards)
print(f'Shuffled cards: {shuffled_deck}')

one_card = shuffled_deck.pop()
print(f'One card taken: {one_card}')
shuffled_deck.appendleft(one_card)
print(f'Card appended to the left: {shuffled_deck}')
