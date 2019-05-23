import json


RATES_FILE_PATH = r"E:\python\Hello Python\rates.json"


def read_rates():
    """reads JSON file and return dict in format {USD: {EUR: rate}}"""
    with open(RATES_FILE_PATH, 'r') as f:
        return json.load(f)


def write_rates(rates):
    """writes dict of rates to JSON file"""
    with open(RATES_FILE_PATH, 'w') as f:
        json.dump(rates, f)


def compute(amount, from_curr, to_curr):
    """takes currencies pair and amount, returns new amount and final currency"""
    rate = RATES.get(from_curr).get(to_curr)
    if rate:
        return round(float(amount) * rate, 3), to_curr


def update_rates(rates, from_curr, to_curr, rate):
    """modifies rate if it exists, otherwise adds a new rate"""
    new_item = {to_curr: rate}
    if rates.get(from_curr):
        new_rate = rates[from_curr]
        new_rate.update(new_item)
        rates[from_curr] = new_rate
    else:
        rates[from_curr] = new_item


def add_reverse_rates(rates):
    """for each pair of currencies creates reverse pair, e.g. USD/EUR -> EUR/USD"""
    rates_copy = dict(rates)
    for from_curr in rates_copy:
        for to_curr, rate in rates_copy[from_curr].items():
            update_rates(rates, to_curr, from_curr, 1 / rate)


def generate_all_computations(amount, curr):
    """returns a list of amount-currency pairs for each exchange possible"""
    all_comp = []
    for c in RATES.get(curr, {}):
        all_comp.append(compute(amount, curr, c))
    return all_comp


def output(list_of_computed_tuples):
    """helps to print the result smoothly"""
    for item in list_of_computed_tuples:
        print(*item)
    print()


RATES = read_rates(RATES_FILE_PATH)
