def is_palindrome(word_to_check):
    word_length = len(word_to_check)
    i = 0
    while i < word_length:
        if word_to_check[i] != word_to_check[word_length - 1]:
            return False
        i = i + 1
        word_length = word_length - 1
    return True


def read_file(file_name):
    with open(file_name, "r", 1, "utf8") as file:
        content = file.readlines()
    result = set([line.lower().strip() for line in content])
    return result


words = read_file("../dict.txt")

print('Palindromes:\n')

for word in words:
    if is_palindrome(word):
        print(word)