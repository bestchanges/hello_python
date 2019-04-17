from rates import exchange, quotes, set_quote


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
                set_quote(pair, quote)
                print(f"Add {pair} = {quote}")
            elif ' ' in user_input:
                volume, base_currency = user_input.split(' ')
                base_currency = base_currency.upper()
                converted = exchange(float(volume), base_currency)
                for result in converted:
                    volume, currency = result
                    print(f"{volume:.2f} {currency}")
        except Exception as e:
            print("Cannot process your request: " + str(e))


if __name__ == '__main__':
    main()