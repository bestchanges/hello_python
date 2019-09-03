from collections import namedtuple

import female
import human
import parent


class Male(human.Human):
    def __init__(self, name, age):
        human.Human.__init__(self, name, age)
        self.sex = human.Sex.MALE

    def __mod__(self, another_female):
        if isinstance(another_female, female.Female):
            # TODO: implement probability
            parents = namedtuple('parents', 'father, mother')
            parents.father = Father(self.name, self.age, [])
            parents.mother = female.Mother(another_female.name, another_female.age, [])
            return parents
        else:
            raise NotImplementedError('We are not there yet.')

    def __and__(self, another_female):
        if isinstance(another_female, female.Female):
            newlywed = namedtuple('newlywed', 'husband, wife')
            newlywed.wife = female.Wife(another_female.name, another_female.age, another_female.children, None)
            newlywed.husband = Husband(self.name, self.age, self.children, None)
            newlywed.wife.husband = newlywed.husband
            newlywed.husband.wife = newlywed.wife
            return newlywed
        else:
            raise NotImplementedError('We are not there yet.')


class Father(parent.Parent, Male):
    def __init__(self, name, age, children):
        parent.Parent.__init__(self, name, age, children)
        Male.__init__(self, name, age)


class Husband(Father):
    def __init__(self, name, age, children, the_wife):
        Father.__init__(self, name, age, children)
        if the_wife is None or isinstance(the_wife, female.Wife):
            self.wife = the_wife
        else:
            raise ValueError('Wife must be of a type Wife')

    def __str__(self):
        return f'{Father.__str__(self)}, Wife: {self.wife.name}'
