from datetime import datetime
import time


class Human():
    def __init__(self, born, name):
        self.born = born
        self.name = name

    def age(self):
        return datetime.now() - self.born


class Male(Human):
    pass

class Female(Human):
    pass

class Family():
    pass

class FamilyMember():
    pass

class Husband(Male, FamilyMember):
    pass

class Wife(Female, FamilyMember):
    pass

