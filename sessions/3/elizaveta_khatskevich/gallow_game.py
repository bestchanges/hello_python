# coding: utf-8
import random
WORDS = '../../2/dict.txt'


def game(number_of_attempts):
    guessed_chars = set()
    guessed_word = random_line(WORDS).lower()
    guessed_word_example = ['_'] * len(guessed_word)
    print('Your word is {}'.format(' '.join(guessed_word_example)))
    while number_of_attempts != 0:
        input_character = enter_a_char()
        if input_character in guessed_chars:
            print('You\'ve already entered this letter.\nLetters you\'ve entered: {}'.format(' '.join(guessed_chars)))
        elif input_character in guessed_word:
            for ind, char in enumerate(guessed_word):
                if input_character == char:
                    guessed_word_example[ind] = input_character
            print('Correct guess!\nAttempts left: {}\nYour word is: {}'.format(number_of_attempts,
                                                                               ' '.join(guessed_word_example)))
            print_death(number_of_attempts)
            if guessed_word_example.count('_') == 0:
                print('You win!')
                break
        else:
            number_of_attempts -= 1
            print('Incorrect guess!\nAttempts left: {}\nYour word is: {}'.format(number_of_attempts,
                                                                                 ' '.join(guessed_word_example)))
            print_death(number_of_attempts)
        guessed_chars.update(input_character)
    if number_of_attempts == 0:
        print(f'Sorry, you loose! The word was: {guessed_word}')


def enter_a_char():
    while True:
        char = input('Please enter a character: ')
        if len(char) != 1:
            print('Please enter one character!')
        else:
            return str(char)


def random_line(afile):
    with open(afile, encoding='utf_8') as f:
        return random.choice(f.read().splitlines())


def general_menu():
    while True:
        choice = input('Would you like to play a new game? (y/n)? ')
        if choice == 'y' or choice == 'Y':
            game(10)
        elif choice == 'n' or choice == 'N':
            print('Bye!')
            break
        else:
            print('Please enter "y" or "n" to continue...')


def print_death(param):
    if param == 10:
        print('\n\n\n\n\n\n')
    elif param == 9:
        print('\n\n\n\n\n\n^^^^^^^^^')
    elif param == 8:
        print('|\n|\n|\n|\n|\n|\n^^^^^^^^^')
    elif param == 7:
        print('______\n|\n|\n|\n|\n|\n^^^^^^^^^')
    elif param == 6:
        print('______\n|\n|\n|\n|  /\n| /\n^^^^^^^^^')
    elif param == 5:
        print('______\n|\n|\n|\n|  /\\\n| /  \\\n^^^^^^^^^')
    elif param == 4:
        print('______\n|\n|\n|  ||\n|  /\\\n| /  \\\n^^^^^^^^^')
    elif param == 3:
        print('______\n|\n|\n| /||\n|  /\\\n| /  \\\n^^^^^^^^^')
    elif param == 2:
        print('______\n|\n|\n| /||\\\n|  /\\\n| /  \\\n^^^^^^^^^')
    elif param == 1:
        print('______\n|\n|   O\n| /||\\\n|  /\\\n| /  \\\n^^^^^^^^^')
    elif param == 0:
        print('______\n|   |\n|   O\n| /||\\\n|  /\\\n| /  \\\n^^^^^^^^^')


if __name__ == "__main__":
    general_menu()
