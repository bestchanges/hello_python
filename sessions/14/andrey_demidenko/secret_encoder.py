
class SecretEncoder():
    def __init__(self, secret_set: dict):
        keys = str.join('', secret_set.keys())
        values = str.join('', secret_set.values())
        self.encode_table = str.maketrans(keys, values)
        self.decode_table = str.maketrans(values, keys)

    def encode(self, text: str):
        return text.translate(self.encode_table)

    def decode(self, text: str):
        return text.translate(self.decode_table)
    

if __name__ == '__main__':
    secret_encoder = SecretEncoder({'a': '$', 'b': '@', 'c': '*', 'd': '!', 'e': ';', 'f': '.', 'g': ',', 'h': ']', 'o': '(', 'r': '%'})
    input_str = input('Enter the string: ')
    encoded_str = secret_encoder.encode(input_str)
    print(f"Encoded string: \t {encoded_str}")
    print(f"Decoded string: \t {secret_encoder.decode(encoded_str)}")