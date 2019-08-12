import argparse
import logging
import os
import runpy
from collections import ChainMap
from logging.handlers import TimedRotatingFileHandler

import imported

file_handler = TimedRotatingFileHandler("app.log", when='midnight', interval=1, backupCount=10)
file_handler.suffix = "%Y-%m-%d"
logging.basicConfig(
    format='%(asctime)s.%(msecs)03d - %(levelname)s [%(filename)s:%(lineno)s %(funcName)10s] %(message)s',
    datefmt="%H:%M:%S",
    level=logging.INFO,
    handlers=[logging.StreamHandler(), file_handler]
)
logging.getLogger('imported').setLevel(logging.DEBUG)


class ArgumentParserWithDefaults(argparse.ArgumentParser):
    """
    This ArgumentParser add ability to use arbitrary mapping object as default values for arguments.
    It can be ChainMap for multiple sources of values (os.environ, config files, classes etc.)
    Note that argument names should be uppercased with dashed '-' replaced by underscore '_'
    """
    def __init__(self, defaults_dict, **kwargs):
        self.defaults_dict = defaults_dict
        super().__init__(formatter_class=argparse.ArgumentDefaultsHelpFormatter, **kwargs)

    def _add_action(self, action):
        action.default = self.defaults_dict.get(action.dest.upper(), action.default)
        return super()._add_action(action)


config_filename = os.environ.get('CONFIG_FILE', 'settings.py')
config_defaults = ChainMap(
    os.environ, # first lookup defaults in environment variables
    runpy.run_path(config_filename) # next lookup in config file
)

# Let's configure argument parser
parser = ArgumentParserWithDefaults(
    description="Here is the good app. "
                "You can use environment variables to set any argument. " \
                "For example for --some-string use var SOME_STRING",
    defaults_dict=config_defaults,
)
parser.add_argument('--host', default="127.0.0.1", help='Address bind to')
parser.add_argument('--port', default=8000, type=int, help='Listening port')
parser.add_argument('--some-int', type=int, required=False, help='int')

# Do actual parse
args = parser.parse_args()

logging.info(args)
logging.info("Listening on %s:%s", args.host, args.port)

imported.some_f()
imported.raised()
logging.info("Work done")