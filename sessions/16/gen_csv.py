import csv
import random
from collections import namedtuple

Person = namedtuple("Person", 'first_name, last_name, sex, age, height')
sex_types = ("Male", "Female")
female_names = "Matilda Vasilisa Veronika Eugenia Julia Joy".split()
male_names = "Svyatoslav Nikifor Lev Ruslan Mikhail Roman".split()
last_names = "Petrov Ivanov Lukashov Zorg Goose Polonev Rekasto Mikhailov Kolal Vorobey Reznikov".split()


def record_generator() -> Person:
    while True:
        sex = random.choice(sex_types)
        first_name = random.choice(male_names if sex == 'Male' else female_names)
        last_name = random.choice(last_names)
        if sex == 'Female' and last_name.endswith("v"):
            last_name += 'a'
        age = random.randint(18, 95)
        height = random.randint(150, 210)
        yield Person(first_name, last_name, sex, age, height)


generator = record_generator()
with open('people.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(Person._fields)
    for _ in range(30):
        person = next(generator)
        print(person)
        writer.writerow(person)