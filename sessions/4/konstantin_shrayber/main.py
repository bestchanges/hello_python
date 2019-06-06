import rates

current_rates = rates.load_current_rates()

print(current_rates)

is_continue = True

while is_continue:
    input_string = input("input: ")

    if input_string == 'quit':
        is_continue = False
    else:
        if " " in input_string:
            for s in rates.calculate_currency_values(current_rates, input_string):
                print(s)
        elif r"/" in input_string and "=" in input_string:
            current_rates = rates.update_currency_rates(current_rates, input_string)
            print("updated!")
            print(current_rates)
        else:
            print("Use only allowed notation! <amount> <currency> to convert; <cur1>/<cur2>=<rate> to setup")