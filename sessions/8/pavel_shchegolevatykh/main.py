from male import Male
from female import Female
from boy import Boy
from girl import Girl

john = Male('John', 32)
print(f'Lonely man: {john}')

martha = Female('Martha', 54)
print(f'Lonely woman: {martha}')

parents = john % martha
print(f'Then they had sex and become {type(parents.mother).__name__} and {type(parents.father).__name__}')

print('9 months passed')

bill = Boy('Bill', 0, parents.father, parents.mother)
amy = Girl('Amy', 0, parents.father, parents.mother)
print('Some kids were born:')
print(f'{type(bill).__name__}: ({bill})')
print(f'{type(amy).__name__}: ({amy})')
print('Now both of them have children:')
parents.mother.children.append(bill)
parents.mother.children.append(amy)
parents.father.children.append(bill)
parents.father.children.append(amy)
print(parents.mother)
print(parents.father)

newlywed = parents.mother & parents.father
print(f'Finally they decided to get married and become {type(newlywed.husband).__name__} \
and {type(newlywed.wife).__name__}')
print(newlywed.husband)
print(newlywed.wife)


