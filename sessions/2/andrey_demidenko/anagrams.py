def start_program():
    anagrams = {}
    with open('../dict.txt', encoding="utf-8") as file:
        words = {line.rstrip(): 1 for line in file}

    for word in words:
        for i in range(1, len(word)-1):
            possible_anagram = word[i:] + word[:i]
            if possible_anagram != word and possible_anagram in words:
                anagrams[word] = possible_anagram

    for main_word, anagram_word in anagrams.items():
        print(main_word + ' - ' + anagram_word)


if __name__ == '__main__':
    start_program()
