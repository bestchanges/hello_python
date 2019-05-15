import random


def read_file(path):
    with open(path, encoding='utf-8') as inputStream:
        words = inputStream.read().splitlines()
        return words


def gallow_game(word):
    encrypted = []
    for x in range(len(word)):
        encrypted.append('*')
    tryNumber = 10
    while True:
        if tryNumber == 0:
            print("Alas, you wasn't able to guess a word :", word)
            break
        if '*' not in encrypted:
            print("Congratulations! You correctly guessed the word:", word)
            break
        print('Try number: ', tryNumber)
        print('Your word: ', ''.join(encrypted))
        char = input('Guess a letter\n')
        if len(char) != 1:
            print('Unexpected input. Please enter 1 character')
            tryNumber -= 1
        elif char not in word:
            print("Word doesn't contain entered character")
            tryNumber -= 1
        elif char in encrypted:
            print('You have already opened this character')
            tryNumber -= 1
        else:
            for x in range(0, len(word)):
                if char == word[x]:
                    encrypted[x] = char


words = read_file('../../2/dict.txt')
word = words[random.randint(0, len(words))]

gallow_game(word)
