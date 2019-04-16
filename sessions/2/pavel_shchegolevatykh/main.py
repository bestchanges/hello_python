def is_palindrome(word_to_check):
    reversed_word = word_to_check[::-1]
    if reversed_word == word_to_check:
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
