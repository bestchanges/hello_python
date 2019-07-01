import json
from re import match
from sys import exit


currency_data = "./exchange_rate.json"


def parse_new_rate(rate):
    if match(r"[A-Z]{3}/[A-Z]{3}=.+", rate):
        currency, value = rate.split("=")
        try:
            new_rate = {currency: float(value)}
            return new_rate
        except ValueError:
            print(f"Invalid currency rate value: {value}. Number is expected")
    else:
        print(f"Invalid currency rate format: {rate}.\n"
              f"Expected format: [Currency 1/Currency 2]=[Rate], e.g. GBP/EUR=1.11791")


def parse_convert_request(convert_request):
    if match(r"\d+(\.\d+)?\s[A-Z]{3}$", convert_request):
        amount, currency = convert_request.split()
        to_convert = {'amount': float(amount),
                      'from': currency}
        return to_convert
    else:
        return None


def get_exchange_rates():
    try:
        with open(currency_data) as json_data:
            exchange_rate = json_data.read()
            return json.loads(exchange_rate)

    except FileNotFoundError:
        exit(f"File '{currency_data}' is not found")


def add_new_rate(rate):
    exchange_rates = get_exchange_rates()
    new_rate = parse_new_rate(rate)
    if new_rate is not None:
        exchange_rates.update(new_rate)
        return exchange_rates


def update_exchange_rates(exchange_rates):
    if exchange_rates is not None:
        try:
            with open(currency_data, "w") as json_data:
                updated_rates = json.dumps(exchange_rates, indent=4)
                json_data.write(updated_rates)
                print(f"Exchange rates updated:")
        except FileNotFoundError:
            exit(f"File '{currency_data}' is not found")
    else:
        print("Failed to update exchange rates")


def print_exchange_rates():
    rates = get_exchange_rates()
    for currency_pair, value in rates.items():
        print(f"{currency_pair}: {value}")


def convert_currency(convert_input):
    request = parse_convert_request(convert_input)
    rates = get_exchange_rates()
    if request is not None:
        is_found = None
        for currency_pair, rate in rates.items():
            currency_in, currency_out = currency_pair.split("/")
            if currency_pair.startswith(request['from']):
                print(f"{request['amount']} {request['from']} = {request['amount']*rate} {currency_out}")
                is_found = True
            elif currency_pair.endswith(request['from']):
                converted = 1 / rate * request['amount']
                print(f"{request['amount']} {request['from']} = {converted} {currency_in}")
                is_found = True
        if not is_found:
            print(f"No exchange rates for {request['from']}")
    else:
        print(f"Invalid input: {convert_input}.\n"
              f"Expected format: [Amount] [Currency Code], e.g. 100 USD")
