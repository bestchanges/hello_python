from collections import namedtuple
from statistics import mean

People = namedtuple('People', ['first_name', 'last_name', 'sex', 'age', 'height'])
list_of_people = []

with open('people.csv', 'r') as file:
    file.readline()
    for line in file:
        person = line.rstrip().split(',')
        list_of_people.append(People(person[0], person[1], person[2], person[3], person[4]))

print('average women age is', round(mean([int(x.age) for x in list_of_people if x.sex == 'Female']), 2))

list_of_people.sort(key=lambda x: int(x.height), reverse=True)
print('top 3 sorted by height desc')
for i in range(3):
    print(list_of_people[i])
