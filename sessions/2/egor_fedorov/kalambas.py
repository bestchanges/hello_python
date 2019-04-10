kalambas, words, reversi = ({}, {}, [])

with open("dict.txt") as file:
    for line in file:
        words[line.rstrip()] = 1

for word in words:
    if len(word) > 3 and word == word[::-1]:
        reversi.append(word)
    for variant in (word[i:] + word[0:i] for i in range(1, len(word)-1)):
        if len(word) > 2 and variant != word and variant in words and not word in kalambas and not variant in kalambas:
            kalambas[word] = variant
            print(word+" "+variant)

print("\nREVERS:\n" + "\n".join(reversi))
print("найдено каламб " + str(len(kalambas)))
print("найдено реверс " + str(len(reversi)))