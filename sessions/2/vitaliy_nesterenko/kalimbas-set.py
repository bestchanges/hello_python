#!#/bin/bash
import time

# variables
input_dict = '../dict.txt'  # input file
min_limit = 3               # min word length
max_limit = 15              # max word length
words_set = set()
result = []


# read file line by line to set function
def __read_file(file, w_set):
    with open(file, encoding='utf-8') as f:
        for line in f:
            w_set.add(line.strip().lower())
        return w_set


# looking for palindroms
def __find_palindroms(w_set, res):
    for word in w_set:
        if min_limit <= len(word) <= max_limit:
            if word == word[::-1]:  # revert the string
                res.append((word, word))  # append array


# generator which is shifting the word
def __gen_shift(word):
    i = 1
    l_word = len(word)
    while i < l_word:
        mod_w = word[i:] + word[:i]
        i += 1
        yield mod_w


# parsing set
def __find_round_sound(w_set, res):
    for word in w_set:
        if min_limit <= len(word) <= max_limit:
            for shifted_word in __gen_shift(word):
                if shifted_word in w_set:
                    res.append([word, shifted_word])


# MAIN
# read file
words_set = __read_file(input_dict, words_set)

# find palindroms
print("Looking for palindroms.")
start = time.time()
__find_palindroms(words_set, result)
end = time.time()
print("Function execution time: ", end - start)

# find round sound words
print("Looking for round sound words.")
start = time.time()
__find_round_sound(words_set, result)
end = time.time()
print("Function execution time: ", end - start)


# final results
print("Final result:", result)