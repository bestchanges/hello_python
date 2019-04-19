import rates


def print_rates(exchange_rates_to_print):
    print('output:')
    for rate in exchange_rates_to_print:
        print(f'{rate[0]} {rate[1]}')


def get_rates():
    value_to_convert = input('input value to check (e.g. 10 USD): ')
    processed_value = value_to_convert.split(' ', 1)
    try:
        amount = float(processed_value[0])
        currency = processed_value[1].upper()
    except ValueError:
        print('Input string is not in proper format')
    exchange_rates = rates.get_exchange_rates(amount, currency)
    print_rates(exchange_rates)


def parse_rate_value(raw_value):
    currencies = raw_value.split('/', 1)
    currency_from = currencies[0].upper()
    currency_to = currencies[1].split('=')[0].upper()
    try:
        rate_amount = float(raw_value.split('=', 1)[1])
    except ValueError:
        print('Input string is not in proper format')
    return {'from': currency_from, 'to': currency_to, 'rate': rate_amount}


def convert_to_string(rate_value):
    return f'{rate_value["from"]}/{rate_value["to"]}={rate_value["rate"]}\n'


def add_or_update_rates():
    value_to_enter = input('Please enter value to add or update (e.g. USD/EUR=3): ')
    rate_value = parse_rate_value(value_to_enter)
    rates.add_or_update_exchange_rate(rate_value)


def load_rates(file_name):
    with open(file_name, "r") as file_handle:
        content = file_handle.readlines()
    result = list([parse_rate_value(line.lower().strip()) for line in content])
    return result


def save_rates(file_name, data):
    proper_lines = (convert_to_string(item) for item in data)
    with open(file_name, "w") as file_handle:
        file_handle.writelines(proper_lines)


try:
    loaded_exchange_data = load_rates('rates.txt')
    rates.exchange_data = loaded_exchange_data
except FileNotFoundError:
    pass

while True:
    action = input('Please select action (1 - check rates, 2 - add/update rates, anything else to exit): ')
    if action == '1':
        get_rates()
    elif action == '2':
        add_or_update_rates()
    else:
        print('Invalid action, exiting..')
        break
save_rates('rates.txt', rates.exchange_data)
