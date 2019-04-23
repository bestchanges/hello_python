import rates

rates.load()
print("input amount and currency to convert (e.x. 10 USD) or update the quotes (e.x. USD/EUR=30.30)")
while True:
    user_input = input("> ")

    try:
        if "=" in user_input:
            currencies_pair, amount = user_input.split("=")
            rates.update(currencies_pair, float(amount))
        elif " " in user_input:
            amount, currency = user_input.split(" ")
            rates.convert(float(amount), currency)
        elif user_input == "exit":
            break
    except Exception as e:
        print("Error occur: {}".format(e))
rates.save()
