import requests


def currency_converter(value, from_cur, to_currency):
    url = f'https://api.exchangerate-api.com/v4/latest/{from_cur.upper()}'
    response = requests.get(url, timeout=5)
    if not response.ok:
        return f'Provided currency {from_cur} does not exist!'
    base = response.json()['rates']
    try:
        value = float(value)
        data = base[to_currency.upper()]
        return f"You get {value * data:.2f} {to_currency}"
    except KeyError:
        return f'Destination currency not found! You have other choices:\n {base.keys()}\n'
    except ValueError:
        return f'Invalid type for value. You gave {value}'


def world_splitter(text):
    return text.split()


def btc_to_rub(value):
    try:
        value = float(value)
        return value * 325960
    except ValueError:
        print(f'Invalid type for value. You gave {value}')

