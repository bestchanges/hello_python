import random

TRIES_LIMIT = 10


def start_game():
    with open('../../2/dict.txt', encoding="utf-8") as file:
        words = [line.rstrip() for line in file]

    random_word = origin_word = {index: value for index, value in enumerate(random.choice(words))}
    hidden_word = {index: '*' for index in range(len(random_word))}
    tries = TRIES_LIMIT
    match_letters = 0

    print('Guess the word: ' + ''.join(hidden_word.values()))
    while True:
        letter = input('Choose a letter: ')
        found = False
        for index, value in random_word.items():
            if letter == value:
                hidden_word[index] = value
                match_letters += 1
                random_word[index] = '*'
                found = True
        if not found:
            tries -= 1
            print(f'Letter is missing, tries left - {tries}')

        print('The word: ' + ''.join(hidden_word.values()))

        if not tries:
            print('You lose. The word was: {}'.format(''.join(origin_word.values())))
            break
        if match_letters == len(hidden_word):
            print('You win !')
            break


if __name__ == '__main__':
    start_game()
