# Terminology from https://en.wikipedia.org/wiki/Currency_pair

quotes = {
    'USD/RUR': 64.35,
    'BTC/RUR': 325960,
    'USD/EUR': 0.88,
    'EUR/RUR': 72.72,
}


def exchange(value, base_currency, quote_currency):
    pair = base_currency + '/' + quote_currency
    if pair in quotes:
        return value * quotes[pair]
    reverse_pair = quote_currency + '/' + base_currency
    if reverse_pair in quotes:
        return 1 / quotes[reverse_pair] * value
    return None


def convert(pair, value):
    if pair in quotes:
        return value * quotes[pair]
    return None


def all_quote_currencies():
    result = set()
    for pair in quotes.keys():
        base, quote = pair.split('/')
        result.add(quote)
    return result


def all_base_currencies():
    result = set()
    for pair in quotes.keys():
        base, quote = pair.split('/')
        result.add(base)
    return result


def all_currencies():
    return all_base_currencies() | all_quote_currencies()


def exchange_to_many(value, base_currency):
    result = []
    for pair, rate in quotes.items():
        base, quote = pair.split('/')
        if base == base_currency:
            value_quote = value * rate
            result.append((value_quote, quote))
        elif quote == base_currency:
            value_quote = value * 1 / rate
            result.append((value_quote, base))
    return result


if __name__ == '__main__':
    print(exchange(10, 'USD', 'RUR'))
    print(exchange(10, 'RUR', 'USD'))
    print(exchange_to_many(100000, 'USD'))
    print(all_quote_currencies())
    print(all_base_currencies())
    print(all_currencies())