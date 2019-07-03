from sys import exit
from os import system
from rates import convert_currency, add_new_rate
from rates import print_exchange_rates, update_exchange_rates


def main():
    while True:
        try:
            menu_input = input("\nPlease, select action:\n"
                               "1. Convert From [Currency]\n"
                               "2. Add new exchange rate\n"
                               "3. Exit\n"
                               "------------------------\n"
                               "Enter your choice [1 - 3]: ")

            if menu_input == "1":
                system('clear')
                convert_input = input("Please, enter [Amount] [Currency Code]: ")
                convert_currency(convert_input)

            elif menu_input == "2":
                system('clear')
                rate_input = input("Please, enter a new exchange rate [Currency 1/Currency 2]=[Rate]: ")
                new_rates = add_new_rate(rate_input)
                update_exchange_rates(new_rates)
                print_exchange_rates()

            elif menu_input == "3":
                system('clear')
                exit()
            else:
                system('clear')
                print(f"Invalid choice: {menu_input}")

        except KeyboardInterrupt:
            exit("\nProgram aborted")


if __name__ == "__main__":
    main()
