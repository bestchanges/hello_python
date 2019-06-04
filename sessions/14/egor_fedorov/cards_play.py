import datetime

suits = (u"\u2664", u"\u2665", u"\u2666", u"\u2667")
ranks = tuple(range(6, 11)) + ('J', 'Q', 'K', 'A')
cards = tuple(f'{rank} {suit}' for suit in suits for rank in ranks)


def shuffle(possible_cards, num=100):
    BIG_PRIME = 499
    cards = list(possible_cards)
    for i in range(num):
        card = cards.pop()
        rand = datetime.datetime.now().microsecond * BIG_PRIME * i
        new_pos = rand % len(cards)
        cards.insert(new_pos, card)
    return cards


k1 = shuffle(cards)
k2 = shuffle(cards)

print(k1)
print(k2)

set1 = set(k1[0:10])
set2 = set(k2[0:10])

print(set1)
print(set2)
print("Intersect: ")
print(set1 & set2)
print("Only in set 1: ")
print(set1 - set2)
print("Unique in each set: ")
print(set1 ^ set2)
