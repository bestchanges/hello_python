from time import perf_counter


SUITS = (u"\u2664", u"\u2665", u"\u2666", u"\u2667")
CARD_SEQUENCE = (6, 7, 8, 9, 10, 11, 'J', 'Q', 'K', 'A')

class Deck():

    def __init__(self):
        self.pack = [f"{card} {suit}" for card in CARD_SEQUENCE for suit in SUITS]

    def shuffle_cards(self):
        for _ in range(100):
            pop_index = int(str(perf_counter())[-1:])
            card = self.pack.pop(int(pop_index))
            self.pack.append(card) 

    def pop_cards(self, count: int):
        return set(self.pack[:count])


if __name__ == '__main__':
    deck1 = Deck()
    deck2 = Deck()
    deck1.shuffle_cards()
    deck2.shuffle_cards()
    sequence1 = deck1.pop_cards(10)
    sequence2 = deck2.pop_cards(10)
    print(f'Cards sequence 1: {sequence1}')
    print(f'Cards sequence 2: {sequence2}')
    print(f'Common in seq 1 and 2: {sequence1 & sequence2}')
    print(f'Diff between seq 1 and 2: {sequence1 - sequence2}')
    print(f'Unique sets in seq 1 and 2: {sequence1 ^ sequence2}')
    sequence2 -= sequence1
    print(f'Sequence 1 after removing common with 1: {sequence2}')
    
    
