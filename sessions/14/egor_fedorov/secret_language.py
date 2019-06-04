table = str.maketrans("аоуыэяёюие", "яёюиеаоуыэ")

strings = (
    "раз два три четыре пять вышел зайчик погулять",
    "через море через горы ехал рома на пригоре",
    "двадцать пять да еще пять будет я пошёл считать",
)
for s in strings:
    print(s.translate(table))


print(input("Ваша строка").translate(table))