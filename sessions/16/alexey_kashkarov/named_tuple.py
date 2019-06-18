import csv
from collections import namedtuple
import numpy as np


people = []
with open('../people.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    fields = next(reader)
    Person = namedtuple("Person", fields)
    for p in map(Person._make, reader):
        people.append(p)

avg_female_age = np.mean([int(p.age) for p in people if p.sex == 'Female'])
print(f'{avg_female_age:.2f}')

top_3_tall = sorted(people, key=lambda p: p.height, reverse=True)[:3]
top_3_tall_names = [f'{p.first_name} {p.last_name}' for p in top_3_tall]
print(top_3_tall_names)
