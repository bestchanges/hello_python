import random

NUMBER_OF_TRIES_ALLOWED = 10


def get_long_words_from_file(filename):
    """returns a list of upper case long words"""
    f = open(filename, "r", 1, "utf8")
    words = [word.strip().upper() for word in f if len(word) > 3 and '-' not in word and ' ' not in word]
    return words


def play_game(easy_mode=True):
    hidden_word = random.choice(get_long_words_from_file(r"E:\python\Hello Python 2\dict.txt"))
    word_model = ['_' for char in hidden_word]
    tries_left = NUMBER_OF_TRIES_ALLOWED
    print(f"New hangman game! Guess the word by letters. Total tries: {tries_left}")
    print("let's go! Input a cyrillic letter, please\n", *word_model)
    print()
    if easy_mode:
        guesses = set()
    while True:
        guess = input().strip().upper()
        if len(guess) != 1 or not ('А' <= guess <= 'Я'):
            print("Wrong input, only single cyrillic letters allowed")
            continue
        else:

            if guess in hidden_word:
                pos = 0
                while pos < len(hidden_word) and hidden_word.find(guess, pos) != -1:
                    pos = hidden_word.find(guess, pos)
                    word_model[pos] = guess
                    pos += 1
                if '_' not in word_model:
                    print("You win! The word is", hidden_word)
                    break
                else:
                    print(f"Good catch! Here's what we have now:\n", *word_model)

            else:
                tries_left -= 1
                if tries_left > 0:
                    print(f"Wrong, sorry. You've got {tries_left} tries left.\n")
                    if easy_mode:
                        guesses.add(guess)
                        if len(guesses) > 1:
                            print("Your previous wrong guesses:", *guesses)

                else:
                    print("You,ve lost, sorry! The word was", hidden_word)
                    break

    new_game = input("\nPress Enter to play new game")
    if new_game is not None:
        play_game(easy_mode)


play_game(easy_mode=False)