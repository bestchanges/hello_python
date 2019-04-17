# Terminology from https://en.wikipedia.org/wiki/Currency_pair

quotes = {
    'USD/RUR': 64.35,
    'BTC/RUR': 325960,
    'USD/EUR': 0.88,
    'EUR/RUR': 72.72,
}


def set_quote(pair, rate):
    base, quote = split_pair(pair)
    if not (isinstance(rate, int) or isinstance(rate, float)):
        raise ValueError("Quote shall be numeric")
    reverse_pair = join_pair(quote, pair)
    if reverse_pair in quotes:
        print(f"Delete duplicate reverse pair {reverse_pair}")
        del quotes[reverse_pair]
    quotes[pair] = rate


def split_pair(pair):
    split = pair.split('/')
    if len(split) != 2:
        raise ValueError(f"{pair} must be in form ABC/DEF")
    base, quote = split
    if base != base.upper() or quote != quote.upper():
        raise ValueError(f"{pair} must be in form ABC/DEF")
    return base, quote


def join_pair(base, quote):
    return base + '/' + quote


def exchange(value, base_currency, quote_currency=None):
    if quote_currency is None:
        return exchange_to_all(value, base_currency)
    pair = join_pair(base_currency, quote_currency)
    if pair in quotes:
        return value * quotes[pair]
    reverse_pair = join_pair(quote_currency, base_currency)
    if reverse_pair in quotes:
        return 1 / quotes[reverse_pair] * value
    return None


def exchange_to_all(value, base_currency):
    result = []
    for pair, rate in quotes.items():
        base, quote = split_pair(pair)
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
    print(exchange_to_all(100000, 'USD'))
