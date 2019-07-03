from rates import currency_converter, world_splitter, btc_to_rub


def general_menu():
    while True:
        choice = input('If you want to convert: \n'
                       'USD to RUB, print "1"\n'
                       'BTC to RUB, print "2"\n'
                       'USD to EUR, print "3"\n'
                       'EUR to RUB, print "4"\n'
                       'For custom conversion, print "5"\n'
                       '"Q" to exit\n')
        if choice == '1':
            value = input('How much do you want to convert from USD to RUB?\n')
            print(currency_converter(value, 'USD', 'RUB'))
        elif choice == '2':
            value = input('How much do you want to convert from BTC to RUB?\n')
            print(f"You get: {btc_to_rub(value)} RUB")
        elif choice == '3':
            value = input('How much do you want to convert from USD to EUR?\n')
            print(currency_converter(value, 'USD', 'EUR'))
        elif choice == '4':
            value = input('How much do you want to convert from EUR to RUB?\n')
            print(currency_converter(value, 'EUR', 'RUB'))
        elif choice == '5':
            text = input('Print request in the following manner: \n'
                         '[HOW MUCH] [FROM CURRENCY] [TO CURRENCY]\n')
            words = world_splitter(text)
            try:
                print(currency_converter(*words))
            except TypeError:
                print('Not enough data for currency conversion!')
        elif choice == 'q' or choice == 'Q':
            print('Bye!')
            break
        else:
            print('Please enter relevant choice!')


if __name__ == "__main__":
    general_menu()
