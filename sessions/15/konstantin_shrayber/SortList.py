people = []

def create_and_add_person(name: str, surname: str, age: int):
    person = dict(name=name, surname=surname, age=age)
    people.append(person)

create_and_add_person('vasya', 'petrov', 24)
create_and_add_person('petya', 'ivanov', 43)
create_and_add_person('kolya', 'sidorov', 39)
create_and_add_person('masha', 'zhukova', 21)
create_and_add_person('klava', 'zapolskaya', 34)
create_and_add_person('onufriy', 'rebrov', 50)

print(people)

people.sort(key=lambda x: x['name']+x['surname'])
print('sorted by full name:')
print(people)

people_by_age = sorted(people, key=lambda x: x['age'])
print('sorted by age:')
print(people_by_age)