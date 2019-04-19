import random


def read_file(file_name):
    with open(file_name, "r", 1, "utf8") as file:
        content = file.readlines()
    result = set([line.lower().strip() for line in content])
    return result


def is_word_guessed(word, letters):
    return set(word) == set(letters)


def print_word_with_placeholders(word, letters):
    print("Word:", end='')
    for letter in word:
        if letter in letters:
            print(f' {letter}', end='')
        else:
            print(' _', end='')
    print('')


def run_round(word_for_this_round):
    attempts_left = NUMBER_OF_GUESSES
    guessed_letters = set()
    missed_letters = set()
    print_word_with_placeholders(word_for_this_round, guessed_letters)
    while attempts_left != 0:
        print('Guess a letter: ', end='')
        input_letter = input()[0]
        if input_letter in word_for_this_round:
            guessed_letters.add(input_letter)
            if is_word_guessed(word_for_this_round, guessed_letters):
                break
        elif input_letter not in missed_letters:
            missed_letters.add(input_letter)
            attempts_left -= 1
        print('')
        print_word_with_placeholders(word_for_this_round, guessed_letters)
        print(f'Guesses: {guessed_letters if guessed_letters else ""}')
        print(f'Misses: {missed_letters if missed_letters else ""}')
        print(f'Attempts left: {attempts_left}')

    if is_word_guessed(word_for_this_round, guessed_letters):
        print(f'Congrats, the word was: {word_for_this_round}')
    else:
        print(f'Game over, the word was: {word_for_this_round}')


def start_game():
    print('The new word is chosen.')
    word_to_guess = random.choice(words)
    run_round(word_to_guess)
    print('')
    print('Start a new game(y/n)? ', end='')
    wish = input()[0]
    print('')
    return wish


NUMBER_OF_GUESSES = 9

words = tuple(read_file("../dict.txt"))

last_wish = 'y'
while last_wish == 'y':
    last_wish = start_game()
