from collections import namedtuple

Person = namedtuple('Person', ['first_name', 'last_name', 'sex', 'age', 'height'])


def string_to_person(raw_value):
    values = raw_value.split(',')
    return Person(values[0], values[1], values[2], int(values[3]), int(values[4]))


def person_to_string(person):
    return f'{person.first_name},{person.last_name},{person.age},{person.sex},{person.height}\n'


def load_people(file_name):
    with open(file_name, "r") as file_handle:
        next(file_handle)
        content = file_handle.readlines()
    result = list([string_to_person(line.strip()) for line in content])
    return result


all_people = load_people('../people.csv')

female_ages = [x.age for x in all_people if x.sex == 'Female']
avg_female_age = sum(female_ages) / len(female_ages)
print(f'Average female age: {avg_female_age}')

top3_height_people = sorted(all_people, key=lambda x: x.height, reverse=True)[:3]
print(f'Top 3 height people: {top3_height_people}')
