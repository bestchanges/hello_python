import random
from contextlib import contextmanager
from datetime import datetime, date, timedelta

# https://backtothefuture.fandom.com/wiki/Back_to_the_Future_timeline
from random import randint

now = datetime.today()


class Human():
    def __init__(self, firstname, lastname, born_at=None):
        global now
        self.born = born_at or now
        self.firstname = firstname
        self.lastname = lastname

    @property
    def age(self, compare_to=None):
        if compare_to is None:
            compare_to = now
        return compare_to - self.born

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"


class Male(Human):
    def __and__(self, female):
        return Family(self, female)

    def sex_with(self, female, preserved: bool, pregnancy_propabilty=None):
        if not pregnancy_propabilty:
            fecundability = 0.2
            # TODO: take ovulation in consideration
            if preserved:
                pregnancy_propabilty = 0.02 * fecundability
            else:
                pregnancy_propabilty = 0.95 * fecundability
        pregnant = random.random() < pregnancy_propabilty
        embryo = HumanEmbryo(self, female) # Male/Female
        female.pregnant_with(embryo)

    def __mod__(self, female):
        return Family(self, female)

class Female(Human):
    pass

class Father:
    pass

class Mother:
    pass

class Family:
    def __init__(self, groom, bride, children=None, born=None):
        assert isinstance(groom, Male)
        assert isinstance(bride, Female)
        self.chidren = children or []
        self.born = born or now
        self.husband = groom # TODO: add Husband mixin
        self.wife = bride # TODO: add Wife mixin

    def __str__(self) -> str:
        return f"Family of {self.husband.lastname}. Marriage registered={self.born} Husband={self.husband}, Wife={self.wife}, Children={self.chidren}"


class FamilyMember:
    pass

class Husband(FamilyMember):
    pass

class Wife(FamilyMember):
    pass


if __name__ == '__main__':
    now = date(1968, 7, 12)
    marty = Male(firstname="Marty", lastname="McFly")
    now = date(1968, 10, 29)
    jennifer = Female(firstname="Jennifer", lastname="Parker")
    now = date(1994, 1, 1)
    mcfly_family = marty & jennifer
    now = date(1995, 1, 1)
    print(now)
    now += timedelta(days=randint(1,354))
    print(now)
    marty % jennifer
    print(mcfly_family)
