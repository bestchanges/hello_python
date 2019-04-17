from rates import exchange, quotes

def main():
    while True:
        user_input = input('Volume and currency: ')
        if not user_input:
            print("Bye")
            break
        try:
            if '=' in user_input:
                pair, value = user_input.split('=')
                quote = float(value)
                quotes[pair] = quote
                print(f"Add {pair} = {quote}")
            volume, base_currency = user_input.split(' ')
            converted = exchange(float(volume), base_currency)
            for result in converted:
                volume, currency = result
                print(f"{volume:.2f} {currency}")
        except:
            print("Cannot process your request")

if __name__ == '__main__':
    main()