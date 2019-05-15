def read_file(path):
    with open(path, encoding='utf-8') as inputStream:
        words = inputStream.read().splitlines()
        return words


def is_anagram(str, str1):
    return sorted(str) == sorted(str1)


def print_anagrams(words):
    for i in range(0, len(words) - 1):
        if is_anagram(words[i], words[i + 1]):
            print(words[i], words[i + 1])


words = read_file('../dict.txt')
print_anagrams(words)
