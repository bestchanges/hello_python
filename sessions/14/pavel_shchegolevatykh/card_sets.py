from collections import namedtuple
import uuid


Card = namedtuple('Card', ['value', 'suit'])


def ranks(): return ['Ace', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']


def suits(): return ['Clubs', 'Diamonds', 'Hearts', 'Spades']


def shuffle(deck): return sorted(deck, key=lambda x: uuid.uuid4())


def create_deck(): return [Card(rank, suit) for rank in ranks() for suit in suits()]


deck1 = shuffle(create_deck())
deck2 = shuffle(create_deck())

ten_cards_deck1 = set(deck1[:10])
ten_cards_deck2 = set(deck2[:10])

print(f'Ten cards from deck1: {ten_cards_deck1}')
print(f'Ten cards from deck2: {ten_cards_deck2}')

common_cards = ten_cards_deck1.intersection(ten_cards_deck2)

print(f'Common cards from both decks: {common_cards}')

deck1_only_cards = ten_cards_deck1.difference(ten_cards_deck2)
deck2_only_cards = ten_cards_deck2.difference(ten_cards_deck1)
print(f'Deck1 cards only: {deck1_only_cards}')
print(f'Deck2 cards only: {deck2_only_cards}')

unique_cards_from_both_decks = ten_cards_deck1.symmetric_difference(ten_cards_deck2)
print(f'Unique cards for both decks: {unique_cards_from_both_decks}')
