import logging

from male import Male
from female import Female
from boy import Boy
from girl import Girl


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
log_formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
log_file_handler = logging.FileHandler('family.log')
log_file_handler.setFormatter(log_formatter)

log_stream_handler = logging.StreamHandler()
log_stream_handler.setFormatter(log_formatter)

logger.addHandler(log_file_handler)
logger.addHandler(log_stream_handler)

john = Male('John', 32)
logger.info(f'Lonely man: {john}')

martha = Female('Martha', 54)
logger.info(f'Lonely woman: {martha}')

parents = john % martha
logger.info(f'Then they had sex and become {type(parents.mother).__name__} and {type(parents.father).__name__}')

logger.info('9 months passed')

bill = Boy('Bill', 0, parents.father, parents.mother)
amy = Girl('Amy', 0, parents.father, parents.mother)
logger.info('Some kids were born:')
logger.info(f'{type(bill).__name__}: ({bill})')
logger.info(f'{type(amy).__name__}: ({amy})')
logger.info('Now both of them have children:')
parents.mother.children.append(bill)
parents.mother.children.append(amy)
parents.father.children.append(bill)
parents.father.children.append(amy)
logger.info(parents.mother)
logger.info(parents.father)

newlywed = parents.mother & parents.father
logger.info(f'Finally they decided to get married and become {type(newlywed.husband).__name__} \
and {type(newlywed.wife).__name__}')
logger.info(newlywed.husband)
logger.info(newlywed.wife)


