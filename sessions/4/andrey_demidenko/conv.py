import rates
import re


def start_app():
    menu = """
Menu:
1 Show quote for amount of currency
2 Show all quotes
3 Set quote for currency
Any key to Exit
"""

    while True:
        print(menu)
        user_input = input('Select option: ')
        if user_input not in '123':
            break

        elif user_input == '1':
            input_amount_currency = input('Enter amount and currency (Example: 10 USD): ')
            regexp = re.match('^(\d*\.\d+|\d*) ([A-Z]{3})$', input_amount_currency)
            if regexp:
                quotes = rates.get_qoutes_for_currency(float(regexp.group(1)), regexp.group(2))
                if len(quotes) == 0:
                    print("There is no quote for selected currency")
                else:
                    for currency, amount in quotes.items():
                        print(f"{amount} {currency}")
            else:
                print('Invalid input')

        elif user_input == '2':
            quotes = rates.get_all_quotes()
            for currency, quote in quotes.items():
                print(f"{currency} = {quote}")

        elif user_input == '3':
            input_quote_currency = input('Enter amount and currencies (Example: USD/RUR=10): ')
            regexp = re.match('^([A-Z]{3}/[A-Z]{3})=(\d*\.\d+|\d*)$', input_quote_currency)
            if regexp:
                rates.set_quote(float(regexp.group(2)), regexp.group(1))
            else:
                print('Invalid input')


if __name__ == '__main__':
    start_app()
