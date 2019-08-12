import time

suits = [u"\u2660", u"\u2665", u"\u2666", u"\u2663"]
ranks = [s for s in range(6, 11)] + ["J", "Q", "K", "A"]
deck = [(r, s) for s in suits for r in ranks]


def shuffle(list):
    for i in range(0, 3 * len(list)):
        pos = str(time.time()).__hash__() % (len(list) - 1)
        card = deck.pop()
        list.insert(pos, card)


set1 = set(deck[0:10])
shuffle(deck)
set2 = set(deck[0:10])

print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"common cards: {set1 & set2}")
print(f"cards present only in set1: {set1 - set2}")
print(f"cards present only in one set: {set1 ^ set2}")
set2 = set2 - set1
print(f"set2 after deleting cards present in set1: {set2}")
