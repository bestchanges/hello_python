import json


class Rates:

    def read_rates(self):
        with open('quotes.json') as rates:
            return json.load(rates)

    def __init__(self):
        self.rates = self.read_rates()

    def print_rates(self, currency, amount):
        if any(currency in s for s in self.rates):
            for currencies in self.rates.keys():
                if currency in currencies:
                    if currencies[0:3] == currency:
                        print(self.rates[currencies] * amount, currencies[4:7])
                    else:
                        print(1 / self.rates[currencies] * amount, currencies[0:3])
        else:
            print("Unknown currency")

    def change_rate(self, currencies, value):
        values = currencies.split("/")
        first = values[0]
        second = values[1]
        if any(first in s and second in s for s in self.rates):
            record = next(x for x in self.rates.keys() if first in x and second in x)
            if record[0:3] == first:
                self.rates[record] = value
            else:
                self.rates[record] = 1 / value
        else:
            self.rates[currencies] = value
        print('Updated rates:', self.rates)

    def save_rates(self):
        with open('quotes.json', 'w') as rates:
            json.dump(self.rates, rates)
        print('Changes have been saved')
