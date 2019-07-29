def caesar_cipher(text, shift=5):
    orig = "".join([chr(x) for r in (range(ord("a"), ord("z")+1), range(ord("A"), ord("Z")+1)) for x in r])
    cipher_table = str.maketrans(orig, orig[shift:]+orig[:shift])
    return text.translate(cipher_table)


orig_text = "Ashes to ashes, funk to funky\n" \
                 "We know Major Tom's a junkie\n" \
                 "Strung out in heaven's high\n" \
                 "Hitting an all-time low\n"
encoded_text = caesar_cipher(orig_text, shift=7)
print(f"encoded:\n{encoded_text}")
decoded_text = caesar_cipher(encoded_text, shift=-7)
print(f"decoded:\n{decoded_text}")
