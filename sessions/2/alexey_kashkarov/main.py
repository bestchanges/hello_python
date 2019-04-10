def generate_anagrams(w):
    result = []
    length = len(w)
    for i in range(1, length):
        result.append(w[-i:] + w[0:length-i])
    return result


def read_file(f_name):
    with open(f_name, "r", 1, "utf8") as f:
        content = f.readlines()
    result = set([x.strip() for x in content])
    return result


words = read_file("../dict.txt")
while len(words) > 0:
    word = words.pop()
    anagrams = generate_anagrams(word)
    for a in anagrams:
        if a in words:
            print(f'{word} - {a}')
