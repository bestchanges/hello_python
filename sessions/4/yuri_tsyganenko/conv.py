#!/usr/bin/env python3

# conv.py - содержит main метод и логику взаимодействия с пользователем, 

from rates import Rates


def set_rate(line):
    parts = line.split('=')
    val = parts[1].strip()
    curr = parts[0].split('/')
    curr_from = curr[0].strip()
    curr_to = curr[1].strip()
    rates.set(curr_from, curr_to, val)

def print_usage():
    print("""Usage:
    value currency                          : conversion,  e.g.: 10 USD
    currency_from / currency_to = value     : to set rate, e.g.: USD/RUB=66
    q : exit
    """)

def main_loop():
    print_usage()
    cmd = ""
    while cmd.strip() != 'q':
        print("> ")
        cmd = input()
        args = cmd.strip().split()
        if len(args) == 2:  # assuming it is, e.g. 10 USD
            rates.calc(args[0], args[1])
        elif '=' in cmd:
            set_rate(cmd)
        else:
            print_usage()


# ========  Execution  =============

rates = Rates()

defaultRates = " USD/RUR=64.35 BTC/RUR=325960 USD/EUR=0.88 EUR/RUR=72.72"

for line in defaultRates.split():
    set_rate(line)

main_loop()



