import exchange
import sys

TIP = "Input 'help' to get a guide"
HELP = "\n".join([
    "================================================================================",
    "help - view this guide",
    "quit - terminate the program",
    "rates - display all rates",
    "forget - remove file with rates",
    "%amount %curr - convert to all known currencies, e.g. 20 USD",
    "%curr/%curr = %rate - set new rate for a pair of currencies, e.g. USD/EUR = 0.93",
    "================================================================================"])


def __main__():
    """waiting for user input to pass it to corresponding helper"""
    print(TIP)

    while True:
        split_inp = input("> ").split()

        if len(split_inp) == 1:
            service_input(split_inp[0])
        elif len(split_inp) == 2:
            convert_input(split_inp)
        elif len(split_inp) == 3:
            update_input(split_inp)
        else:
            print_error()


def service_input(inp: str):
    """handles service words of the program"""
    if inp == 'help':
        print(HELP)
    elif inp == 'quit':
        sys.exit()
    elif inp == 'rates':
        print_rates()
    elif inp == 'forget':
        if exchange.remove_dump():
            print("rates file removed")
        else:
            print("rates file not found")
    else:
        print_error()


def print_rates():
    """output for all known rates"""
    for k in exchange.RATES:
        print(k, exchange.RATES[k])


def print_error(error="error"):
    """receives an error message and displays it along with the tip"""
    print(error, TIP, sep='\n')


def convert_input(inplist: list) -> None:
    """handles input for conversion of amount"""
    amount = get_amount_from_str_and_validate(inplist[0])
    if amount:
        currency = inplist[1].upper()
        if len(currency) != 3:
            print_error("wrong currency, use 3-letter code: USD")
        elif currency in exchange.RATES:
            exchange.output(exchange.convert_to_known_currencies(amount, currency))
        else:
            print_error("unknown currency")


def update_input(inplist: list) -> None:
    """handles input for updating rate"""
    if len(inplist[0]) != 7:
        print_error("currency pair expected: USD/EUR")
    else:
        new_rate = get_amount_from_str_and_validate(inplist[2])
        if new_rate:
            frm = inplist[0][:3].upper()
            to = inplist[0][4:].upper()
            if frm == to:
                print_error(f"cannot set rate from {frm} to {to}")
            else:
                exchange.save_updated_rates(frm, to, new_rate)
                print("rates updated!")
                print_rates()


def get_amount_from_str_and_validate(numstr: str) -> float:
    """validates the amount provided by user and returns zero if it is not correct"""
    result = 0
    try:
        result = float(numstr)
        if result <= 0:
            raise ValueError
    except ValueError:
        print_error("positive numeric amount expected")

    return result if result > 0 else 0


__main__()
