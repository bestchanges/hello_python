#!/usr/bin/env python3

# conv.py - содержит main метод и логику взаимодействия с пользователем, 


def print_usage():
    print("""Usage:
    value currency                          : conversion,  e.g.: 10 USD
    currency_from / currency_to = value     : to set rate, e.g.: USD/RUB=66
    q : exit
    """)

def main_loop():
    print_usage()
    cmd = ""
    while cmd.strip() not in ['q', 'Q']:
        print("> ")
        cmd = input()
        args = cmd.strip().split()
        if len(args) == 2:  # assuming it is, e.g. 10 USD
            rates.calc(args[0], args[1])
        elif '=' in cmd:
            rates.parseRate(cmd)
        else:
            print_usage()
    rates.save()


# ========  Execution  =============

if __name__ == "__main__":
	from rates import Rates
	rates = Rates(" USD/RUR=64.35 BTC/RUR=325960 USD/EUR=0.88 EUR/RUR=72.72")
	main_loop()



