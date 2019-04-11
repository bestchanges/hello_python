import random


def decode_word(word, tries):
    result = ''
    for l in word:
        if l in tries:
            result += l
        else:
            result += '_'
        result += ' '
    return result


def count_tries(word, letters):
    missed = ''
    for l in letters:
        if not l in word:
            missed += l
    return len(missed)


with open('../../2/dict.txt') as f:
    words = f.readlines()
    word = random.choice(words).rstrip()
tried_letters = ""
MAX_TRIES = 10

while True:
    decoded = decode_word(word, tried_letters)
    tries_left = MAX_TRIES - count_tries(word, tried_letters)

    if tries_left <= 0:
        print(f"You loose! It was {decode_word(word, word)}")
        break

    if decoded.find('_') == -1:
        print(f"You win! {decoded}")
        break

    letter = input(f"{decoded} ({tries_left} left): ")
    tried_letters += letter

