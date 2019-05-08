def get_words_from_file(filename):
    """returns a dict with word length as keys and lowercase words in a list for each key"""
    words_by_len = {}
    f = open(filename, "r", 1, "utf8")
    for word in f:
        word = word.strip().lower()
        w_len = len(word)
        if w_len > 1:
            words_by_len[w_len] = words_by_len.get(w_len, []) + [word]
    return words_by_len


def gen_linear_anagram_candidates(word):
    """takes a string and returns a list of its linear permutations, excluding initial word"""
    anagram_candidates = []
    for pos in range(1, len(word)):
        anagram_candidates += [word[pos:] + word[0:pos]]
    return anagram_candidates


def collect_anagrams_set(words_list):
    """returns list of pairs of words that are anagrams to each other"""
    words_set = set(words_list)
    anagrams = []
    while len(words_set) > 0:
        word = words_set.pop()
        anagrams += [word + " - " + anagram for anagram in gen_linear_anagram_candidates(word) if anagram in words_set]
    return anagrams


def __main__():
    for words_of_same_len in get_words_from_file("dict.txt").values():
        anagrams_output = collect_anagrams_set(words_of_same_len)
        if len(anagrams_output) > 0:
            print(*anagrams_output, sep='\n')


__main__()
