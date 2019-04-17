#!/usr/bin/env python3

# методы для вычислений обмена и данные для этого.


class Rates:
    """ calculate rates and handle needed data """

    def __init__(self):
        self.rate = {}

    # Todo implement save-load
    # def load(filename):
    # def save(filename):

    def set(self, curr_from, curr_to, value):
        # todo: any validation? trim?
        # init - in case it is the first assignment
        self.rate.setdefault(curr_from, {})
        self.rate.setdefault(curr_to, {})
        self.rate[curr_from].setdefault(curr_to, {})
        self.rate[curr_to].setdefault(curr_from, {})
        # assign
        self.rate[curr_from][curr_to] = float(value)
        self.rate[curr_to][curr_from] = 1.0 / float(value)


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



