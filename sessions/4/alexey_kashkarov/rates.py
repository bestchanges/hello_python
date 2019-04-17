#imports
import json
import urllib.request as req
import urllib.error

#constants
DEFAULT_RATES_PATH = "./rates.json"

#variables
rates = dict()

#functions
def load_rates(f_path=DEFAULT_RATES_PATH):
    global rates
    with open(f_path) as json_data_file:
        rates = json.load(json_data_file)


def convert(amount, currency):
    assert (amount > 0), "Amount should be positive."
    assert (len(currency) == 3), "Incorrect currency format."
    for k in rates.keys():
        if currency in k:
            i = 0
            if k.find(currency) == 0:
                rate = rates[k]
                i = 4
            elif k.find(currency) > 0:
                rate = 1 / rates[k]
            precision = 6 if k[i:i + 3] == "BTC" else 2
            print(f"{rate * amount:.{precision}f} {k[i:i + 3]}")


def update(currency1, currency2, rate):
    if f"{currency2}/{currency1}" in rates.keys():
        rate = 1 / rate
        rates[f"{currency2}/{currency1}"] = rate
    else:
        rates[f"{currency1}/{currency2}"] = rate


def save_rates(f_path=DEFAULT_RATES_PATH):
    with open(f_path, "w") as json_data_file:
        json.dump(rates, json_data_file, indent=4)


def download(currency1, currency2):
    try:
        content = req.urlopen(f"https://api.exchangeratesapi.io/latest?base={currency2}&symbols={currency1}").read()
        content = content.decode()
        data = json.loads(content)
        rate = data["rates"][currency1]
        update(currency2, currency1, rate)
    except urllib.error.HTTPError as e:
        raise ConnectionError(e)
