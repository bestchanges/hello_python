tran_dict = {'a': '@', 'e': '3', 'h': '4', 'i': '!', 'l': '1', 'n': 'и', 'o': '0', 'q': 'ф', 'r': 'я', 's': '5', 't': '7', 'u': 'й'}
table = str.maketrans(tran_dict)

example_str = "This is example string to translate using leet speak tab"
print(example_str.translate(table))

user_str = input('Please specify your string for leet translate: ')
print(user_str.translate(table))