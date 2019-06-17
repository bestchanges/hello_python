from collections import deque
import random


class Colors:
    RED = '\x1b[91m'
    GREEN = '\x1b[92m'
    YELLOW = '\x1b[93m'
    BLUE = '\x1b[94m'
    END = '\x1b[0m'


def print_deck(title, d):
    print(title)
    output = ''
    for c in d:
        output += c + ' '
    print(output)


suits = [u"\u2660", u"\u2665", u"\u2666", u"\u2663"]
ranks = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
deck = deque([f'{r}{s}' if s in [u"\u2660", u"\u2663"]
              else f'{Colors.RED}{r}{s}{Colors.END}' for r in ranks for s in suits])
print_deck('Original deck:', deck)

random.shuffle(deck)
print_deck('Shuffled deck:', deck)

shift = random.randint(-len(deck), len(deck))
deck.rotate(shift)
print_deck('Shifted deck:', deck)

black_cards = deque(card for card in deck if u"\u2660" in card or u"\u2663" in card)
red_cards = deque(card for card in deck if u"\u2665" in card or u"\u2666" in card)
print_deck('Black cards:', black_cards)
print_deck('Red cards:', red_cards)

deck = black_cards + red_cards
print_deck('Whole deck:', deck)

random.shuffle(deck)
print_deck('Shuffled deck:', deck)

deck.rotate(1)
print_deck('1-card shifted deck:', deck)
