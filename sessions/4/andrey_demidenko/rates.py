import json

initial_quotes = {
    'USD/RUR': 64.35,
    'BTC/RUR': 325960,
    'USD/EUR': 0.88,
    'EUR/RUR': 72.72
}


def get_all_quotes() -> dict:
    try:
        with open('quotes.json', encoding="utf-8") as quotes_file:
            quotes = json.load(quotes_file)

    except IOError:
        quotes = initial_quotes

    return quotes


def get_qoutes_for_currency(amount: float, currency: str) -> dict:
    return {quote[-3:]: value * amount for quote, value in get_all_quotes().items() if quote[:3] == currency}


def set_quote(amount: float, quote: str):
    quotes = get_all_quotes()
    quotes[quote] = amount
    save_quotes(quotes)


def save_quotes(quotes: dict):
    with open('quotes.json', 'w', encoding="utf-8") as quotes_file:
        json.dump(quotes, quotes_file)
