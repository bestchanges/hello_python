import json
import os


RATES_FILE_PATH: str = "rates.json"


def read_rates_from_file():
    """reads JSON file and return dict in format {USD: {EUR: rate}}"""
    with open(RATES_FILE_PATH, 'r') as f:
        return json.load(f)


def write_rates_to_file():
    """writes dict of rates to JSON file, adds gitignore rule for this file"""
    with open(RATES_FILE_PATH, 'w') as f:
        json.dump(RATES, f)
    with open(".gitignore", 'w') as gitignore:
        gitignore.write(RATES_FILE_PATH)


def get_precision(curr: str) -> int:
    """gets a currency and returns precision for it's rate;
    BTC needs to have higher precision, which is too much for other currencies"""
    return 8 if curr == 'BTC' else 4


def convert(amount: float, frm: str, to: str) -> tuple:
    """takes currencies pair and amount, returns new amount and final currency"""
    rate = RATES.get(frm).get(to)
    if rate:
        return round(float(amount) * rate, get_precision(to)), to


def update_rate(frm: str, to: str, rate: float) -> None:
    """modifies rate if it exists, otherwise adds a new rate"""
    if RATES.get(frm):
        RATES[frm][to] = rate
    else:
        RATES[frm] = {to: rate}


def save_updated_rates(frm: str, to: str, rate: float) -> None:
    """updates rate, its reversed pair and saves changes to file"""
    precision = max(get_precision(frm), get_precision(to))
    update_rate(frm, to, rate)
    update_rate(to, frm, round(1/rate, precision))
    write_rates_to_file()


def convert_to_known_currencies(amount: float, curr: str) -> list:
    """returns a list of amount-currency pairs for each exchange possible"""
    all_comp = []
    for c in RATES.get(curr, {}):
        all_comp.append(convert(amount, curr, c))
    return all_comp


def output(list_of_computed_tuples: list):
    """helps to print the result of conversion smoothly"""
    for item in list_of_computed_tuples:
        print(*item)
    print()


def remove_dump() -> bool:
    """removes files created by this script"""
    result = False
    try:
        os.remove(RATES_FILE_PATH)
        os.remove(".gitignore")
        result = True
    except:
        pass
    return result


if os.path.exists(RATES_FILE_PATH):
    RATES = read_rates_from_file()
else:
    RATES = {
        "USD": {"RUR": 64.35, "EUR": 0.88},
        "BTC": {"RUR": 325960},
        "EUR": {"RUR": 72.72}
    }
    write_rates_to_file()


