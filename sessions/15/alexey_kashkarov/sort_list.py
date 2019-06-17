people = [{'first_name': 'John', 'last_name': 'Doe', 'sex': 'M', 'age': 30},
          {'first_name': 'Jane', 'last_name': 'Doe', 'sex': 'F', 'age': 25},
          {'first_name': 'Arnold', 'last_name': 'Schwarzenegger', 'sex': 'M', 'age': 71},
          {'first_name': 'Phillip', 'last_name': 'Fry', 'sex': 'M', 'age': 25}]

people_copy1 = people.copy()
people_copy1.sort(key=lambda p: f'{p["first_name"]} {p["last_name"]}')
print(people_copy1)
people_copy2 = sorted(people, key=lambda p: p['age'])
print(people_copy2)
