#!/usr/bin/python
import random

# variables
input_dict = '../../2/dict.txt'  # input file
words_set = set()                # empty set
tries = 10                       # number of tries


# FUNCTIONS
# read file line by line and return random word
def __read_file(file, w_set):
    with open(file, encoding='utf-8') as f:
        for line in f:
            w_set.add(line.strip().lower())
        return random.choice(tuple(w_set))


def __check_guess(g):  # guess
    global t, word, progress_word
    for i in range(0, len(word)):
        if g == word[i]:
            progress_word[i] = word[i]


# MAIN
# select random word from words_set
word = __read_file(input_dict, words_set)
print("The length of guessed word is %s, the word itself is %s" % (len(word), word))
# temporary word to save the progress
progress_word = [None] * len(word)

# game logic
t = 0  # try

# expose space and dash symbols
__check_guess(' ')
__check_guess('-')

while t <= tries:
    print("-"*30)

    # check if tries has left
    if tries - t == 0:
        print("Game over!")
        break

    # checking if it is a time to finish the game
    if None not in progress_word:
        print("Congratulations! You guessed the word %s! \n%s tries left." % (word, tries -t))
        break

    guess = input("Input the letter: ")

    # user input check
    if len(guess) > 1:
        print("You entered more than 1 char")
        continue
    if guess in progress_word:
        print("You've already guessed that char, please try another one")
        continue
    if guess not in word:
        t += 1
        print("Progress: %s" % progress_word)
        print("Tries left %s" % (tries - t))

    # continue the game
    else:
        print("Your letter is %s" % guess)
        __check_guess(guess)
        print("Progress: %s" % progress_word)
        print("Tries left %s" % (tries - t))