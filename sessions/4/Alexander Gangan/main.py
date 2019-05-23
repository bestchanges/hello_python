import exchange


def parse_input():
    """receives input, returns a result depending on a format"""
    new_input = input("Provide your query or update rate in format USD/EUR = 0.88: \n").split()
    if new_input == ['rates']:
        for k in exchange.RATES:
            print(k, exchange.RATES[k])
            result = {"flag": "rates provided"}
    elif len(new_input) == 2:
        result = {"flag": "compute",
                  "amount": float(new_input[0]),
                  "currency": new_input[1].upper()}
    elif len(new_input) == 3:
        result = {"flag": "update",
                  "from_currency": new_input[0][:3].upper(),
                  "to_currency": new_input[0][4:].upper(),
                  "new_rate": float(new_input[2])}
    else:
        result = {"flag": "error"}
    return result


def __main__():
    while True:
        user_in = parse_input()
        if user_in["flag"] == "compute":
            exchange.output(exchange.generate_all_computations(user_in["amount"], user_in["currency"]))
        elif user_in["flag"] == "update":
            rates_d = exchange.RATES
            f_c = user_in["from_currency"]
            t_c = user_in["to_currency"]
            r = user_in["new_rate"]
            exchange.update_rates(rates_d, f_c, t_c, r)
            exchange.update_rates(rates_d, t_c, f_c, 1/r)
            exchange.write_rates(rates_d)
        else:
            print(user_in["flag"])


__main__()





