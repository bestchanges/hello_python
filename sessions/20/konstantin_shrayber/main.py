import argparse
import logging
import runpy
from collections import ChainMap

import rates

app_defaults = {'log_file': 'exchange_service.log', 'rates_file': 'rates.txt'}
settings_dict = runpy.run_path('settings.py')
settings = ChainMap(settings_dict, app_defaults)
rates.set_params(settings['rates_file'], settings['log_file'])

logger = logging.getLogger('exchangeService')
logger.setLevel(logging.INFO)
fh = logging.FileHandler(settings['log_file']) #'exchange_service.log'
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

parser = argparse.ArgumentParser()
parser.add_argument('--input-string', default='')
args = parser.parse_args()

logger.info('exchange service called')
current_rates = rates.load_current_rates()

print(current_rates)

is_continue = True

while is_continue:
    if len(args.input_string) > 3:
        input_string = args.input_string.replace('_', ' ')
        is_continue = False
        logger.info('command line argument spotted, configured for single execution w. auto quit initiation')
    else:
        input_string = input("input: ")

    if input_string == 'quit':
        is_continue = False
        logger.info('quit initiated')
    else:
        logger.info(input_string + ' value passed for processing')
        if " " in input_string:
            for s in rates.calculate_currency_values(current_rates, input_string):
                print(s)
        elif r"/" in input_string and "=" in input_string:
            current_rates = rates.update_currency_rates(current_rates, input_string)
            print("updated!")
            print(current_rates)
        else:
            print("Use only allowed notation! <amount> <currency> to convert; <cur1>/<cur2>=<rate> to setup")
            logger.info('incorrect value spotted')