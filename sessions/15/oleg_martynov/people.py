class Man:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_age(self):
        return self.age

    def __str__(self):
        return f"{self.firstname} {self.lastname}, {self.age} years old"


people = [Man("Ivan", "Petrov", 30), Man("Ivan", "Ivanov", 25), Man("Ivan", "Sidorov", 18), Man("Petr", "Ivanov", 40),
          Man("Petr", "Sidorov", 27), Man("Petr", "Petrov", 54), Man("Sidor", "Petrov", 36), Man("Sidor", "Ivanov", 22),
          Man("Sidor", "Sidorov", 33)]

people.sort(key=lambda man: (man.get_firstname(), man.get_lastname()))

print("sort by name".center(30, "="))
for man in people:
     print(man)

print()

age_sort = sorted(people, key=Man.get_age)

print("sort by age".center(30,"="))
for man in age_sort:
    print(man)