given_string = 'this is the song lalalala.'
print('Given string:')
print(given_string)
translation_table = given_string.maketrans('abcdefghijklmnopqrstuvwxyz', 'plmoknijbygvtfcrdxeszaqwuh')
print('Translation table:')
print(translation_table)
translated_string = given_string.translate(translation_table)
print('Tanslated string:')
print(translated_string)
