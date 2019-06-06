def read_file(file_path) -> dict:
    with open(file_path, "r", 1, "utf8") as file:
        content = file.readlines()
    result = {}
    for x in content:
        w = x.strip()
        letters = list(w)
        letters.sort()
        result[w] = letters

    return result


words = read_file(r"C:\hello_python-master\sessions\2\dict.txt")

while len(words) > 0:
    word, sorted_letters = words.popitem()
    if sorted_letters in words.values():
        for k in words.keys():
            if sorted_letters == words[k]:
                print(word, " - ", k)