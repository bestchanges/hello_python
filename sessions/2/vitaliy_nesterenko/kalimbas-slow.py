#!/usr/bin/python

import json

dictionary = "../dict.txt"
sorted_dict = dict()
output_dict = dict()
word_length = 0
counter = 0


# FUNCTIONS


def __word_checker(word, array):
    i = 0
    #print(array)
    init_word = word

    for elem in init_word:
        #print("\n" + word)
        i = i + 1
        word = word[-1] + word[0:-1] # [-1] - last element of the word,
                                     # [0:-1] - word without last element
        if i >= len(init_word):
            return {}

        # print(word)
        if word in array:
            # print("%s in %s" % (word, init_word))
            if init_word == word:
                array.remove(init_word)
            else:
                array.remove(init_word)
                array.remove(word)
            return {init_word: word}


# MAIN


with open(dictionary, encoding='utf-8') as f:
    # read file by line
    for line in f:
        # get word length
        word_length = len(line.strip())
        # structure creation
        if str(word_length) not in sorted_dict:
            # create keys for sorted dict
            sorted_dict[str(word_length)] = []
            # create keys for output dict
            output_dict[str(word_length)] = {}
        if word_length > 2:
            # add word to the proper key, delete new line symbols and make all words as lowercase strings
            sorted_dict[str(word_length)].append(line.strip().lower())

# walk through keys
for key in sorted_dict:
    # print(sorted_dict)
    # walk through words in lists
    for i in sorted_dict[key]:
        # update dictionary with final results
        # print(output_dict)
        output_dict[key].update(__word_checker(i, sorted_dict[key]))
        counter = counter + 1
        print(counter)

# write to the file
with open('result.json', 'w', encoding='utf-8') as resultfile:
    json.dump(output_dict, resultfile, ensure_ascii=False, indent=4)