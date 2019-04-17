from rates import exchange_to_many

def main():
    while True:
        user_input = input('Volume and currency: ')
        if not user_input:
            print("Bye")
            break
        volume, base_currency = user_input.split(' ')
        converted = exchange_to_many(float(volume), base_currency)
        for result in converted:
            volume, currency = result
            print(f"{volume:.2f} {currency}")


if __name__ == '__main__':
    main()