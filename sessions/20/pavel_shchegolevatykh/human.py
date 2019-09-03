from enum import Enum


class Sex(Enum):
    UNKNOWN = 0
    MALE = 1
    FEMALE = 2


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sex = Sex.UNKNOWN

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, \
Sex: {"Male" if self.sex == Sex.MALE else "Female" if self.sex == Sex.FEMALE else "Unknown"}'
