import random

dict_array = []

with open("../../2/dict.txt", "r") as dict_file:
    for word in dict_file:
        dict_array.append(word.rstrip())

word_to_guess = random.choice(dict_array)
trial_process = list("_" * len(word_to_guess))

trial_count = 10
win = False
used_chars = set()

print("Попробуйте угадать слово за {} попыток".format(trial_count))

print("{} (осталось попыток {})".format("".join(trial_process), trial_count))
while trial_count > 0:

    char = input()
    if not char.isalpha() or len(char) > 1:
        print("Введите одну букву")
        continue
    if char in used_chars:
        print("Такая буква уже была")
        continue
    used_chars.add(char)
    char_found = False
    for i in range(0, len(word_to_guess)):
        if word_to_guess[i] == char:
            trial_process[i] = char
            char_found = True
    if "_" not in trial_process:
        win = True
        break
    if not char_found:
        trial_count -= 1
    print("{} (осталось попыток {})".format("".join(trial_process), trial_count))

if win:
    print("Вы угадали, загаданное слово: {}".format(word_to_guess))
else:
    print("Вы не угадали, загаданное слово: {}".format(word_to_guess))
