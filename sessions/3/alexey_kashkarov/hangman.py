import random as rnd


def load_dict(fpath):
    words = []
    with open(fpath, "r", 1, "utf8") as f:
        for line in f:
            if len(line) > 3:
                words.append(line.rstrip())
    return words


def get_random_word(words):
    return words[rnd.randint(0, len(words)-1)]


ATTEMPTS = 6
words = load_dict("../../2/dict.txt")
while True:
    word = get_random_word(words)
    guess = ''
    print(f"I made a word of {len(word)} letters\nYou have {ATTEMPTS} attempts to guess it")
    for l in word:
        guess += "*"
    print(f"{guess}\n")
    attempt = 0
    while attempt < ATTEMPTS:
        letter = input("Guess a letter: ")
        i = 0
        found = False
        while i < len(word):
            if word[i] == letter:
                guess = guess[:i] + letter + guess[i + 1:]
                found = True
            i += 1
        if not found:
            attempt += 1
        if word == guess:
            break
        print(f"{guess}\n{ATTEMPTS - attempt} attempts left")
    if attempt < ATTEMPTS:
        print(f"You win with {ATTEMPTS - attempt} attempts left! It was \"{word}\"!")
    else:
        print(f"You lose! It was \"{word}\"!")
    if input("\nPlay again (y/n)?") != "y":
        break
