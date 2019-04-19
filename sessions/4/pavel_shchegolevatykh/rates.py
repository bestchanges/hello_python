exchange_data = [
    {
        "from": "USD",
        "to": "RUR",
        "rate": 64.35
    },
    {
        "from": "BTC",
        "to": "RUR",
        "rate": 325960
    },
    {
        "from": "USD",
        "to": "EUR",
        "rate": 0.88
    },
    {
        "from": "EUR",
        "to": "RUR",
        "rate": 72.72
    }
]


def add_or_update_exchange_rate(rate_value):
    updated = False
    for item in exchange_data:
        if item['from'] == rate_value['from'] and item['to'] == rate_value['to']:
            item['rate'] = rate_value['rate']
            updated = True
    if not updated:
        exchange_data.append(rate_value)


def get_exchange_rates(amount, currency):
    exchange_rates = list()
    for item in exchange_data:
        if item['from'] == currency:
            exchange_rates.append((item['to'], amount * item['rate']))
    return exchange_rates
