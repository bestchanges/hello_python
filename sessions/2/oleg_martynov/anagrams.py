import os


def string_cycler(input_str):
    i = 1
    while i < len(input_str):
        yield input_str[i:] + input_str[:i]
        i += 1


dict = set()

with open('dict.txt') as dict_file:
    for line in dict_file:
        dict.add(line.strip())

result = []

for word in set(w.lower() for w in dict):
    for cycled_word in string_cycler(word):
        if cycled_word in dict and cycled_word != word:
            result.append({word, cycled_word})
        break

print(result)
