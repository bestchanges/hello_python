#!/usr/bin/env python3

import json

# методы для вычислений обмена и данные для этого.


class Rates:
    """ calculate rates and handle needed data """
    filename = 'rates.json'

    # def __init__(self):
    #     self.rate = {}
    #     self.load()

    def __init__(self, initial_rates):
        self.rate = {}
        if not self.load():
            for line in initial_rates.split():
                self.parseRate(line)


    def load(self):
        try:
            with open(Rates.filename, 'rt') as file:
                self.rate = json.load(file)
            return True
        except FileNotFoundError:  # as fnf:
            return False

    def save(self):
        print("Bye!")
        with open(Rates.filename, 'wt') as file:
            json.dump(self.rate, file)

    def set(self, curr_from, curr_to, value):
        # init - in case it is the first assignment
        cto = curr_to.strip()
        cfrom = curr_from.strip()
        self.rate.setdefault(cfrom, {})
        self.rate.setdefault(cto, {})
        self.rate[cfrom].setdefault(cto, {})
        self.rate[cto].setdefault(cfrom, {})
        # assign
        self.rate[cfrom][cto] = float(value)
        self.rate[cto][cfrom] = 1.0 / float(value)

    def parseRate(self, line):
        parts = line.split('=')
        val = parts[1].strip()
        curr = parts[0].split('/')
        curr_from = curr[0].strip()
        curr_to = curr[1].strip()
        self.set(curr_from, curr_to, val)

    def get(self, curr_from, curr_to):
        return self.rate[curr_from][curr_to]


    def curr_list(self):
        return list(self.rate.keys())


    def calc(self, amount, curr_from):
        #  data validation
        if curr_from not in self.curr_list():
            print("{} is unknown. Available currencies: {}".format(curr_from, self.curr_list()))
            return
        assert(amount.isnumeric())  # : ensure amount is
        #  Calculations
        for curr_to, perUnit in self.rate[curr_from].items():
            print("{0:,.02f} {1:}".format(float(amount) * perUnit, curr_to))

#              Error(s):
# >>> u=64.35
# >>> am = "10"
# >>> print("{0:,.02f} {}".format(float(am) * u, 'RUR'))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: cannot switch from manual field specification to automatic field numbering
#
