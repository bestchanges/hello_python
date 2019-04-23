import re
import json

DEFAULT_PATH = "./quotes.json"

quotes = {}


def convert(amount, curr):

    def print_result(amount1, currency1, amount2, currency2):
        print("{} {} = {} {}".format(amount1, currency1, amount2, currency2))

    for rate in quotes.keys():
        currs = rate.split("/")
        if curr in currs:
            if rate.index(curr) == 0:
                print_result(amount, currs[0], amount * quotes.get(rate), currs[1])
            else:
                print_result(amount, currs[1], amount / quotes.get(rate), currs[0])


def update(currencies_pair, quote):
    global quotes
    cp_pattern = re.compile("[A-Z]{3}/[A-Z]{3}")
    if not cp_pattern.match(currencies_pair):
        print("wrong currencies pair")
        return
    quotes.update({currencies_pair: quote})


def save(quotes_path=DEFAULT_PATH):
    with open(quotes_path, "w") as quotes_file:
        json.dump(quotes, quotes_file)


def load(quotes_path=DEFAULT_PATH):
    global quotes
    with open(quotes_path, "r") as quotes_file:
        quotes = json.load(quotes_file)


if __name__ == "__main__":
    load()
    convert(10, "RUR")
    update("USD/RUR", 71.50)
    convert(10, "RUR")
    save()
