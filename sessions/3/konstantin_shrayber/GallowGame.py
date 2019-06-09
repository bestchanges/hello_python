import random

with open(r"C:\hello_python-master\sessions\2\dict.txt", "r", 1, "utf8") as file:
    content = file.readlines()

i = random.randint(1, len(content))

guess_word = content[i].strip()
guessed_ltrs = []

for l in guess_word:
    guessed_ltrs.append("_")

try_attempts = 10
is_success = False

while try_attempts > 0 and is_success is False:
    print(' '.join(guessed_ltrs), '; attempts left: ', try_attempts)
    letter = input('Please guess letter: ')

    if letter in guess_word:
        itr = 0
        while itr < len(guess_word):
            if guess_word[itr] == letter:
                guessed_ltrs[itr] = letter
            itr += 1
    else:
        try_attempts -= 1

    if '_' not in guessed_ltrs:
        is_success = True
        break

if is_success:
    print('You won! ', guess_word)
else:
    print('You lost( Word was: ' + guess_word)