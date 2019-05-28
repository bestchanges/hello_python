from collections import namedtuple

import human
import male
import parent


class Female(human.Human):
    def __init__(self, name, age):
        human.Human.__init__(self, name, age)
        self.sex = human.Sex.FEMALE

    def __mod__(self, another_male):
        if isinstance(another_male, male.Male):
            # TODO: implement probability
            parents = namedtuple('parents', 'father, mother')
            parents.mother = Mother(self.name, self.age, [])
            parents.father = male.Father(another_male.name, another_male.age, [])
            return parents
        else:
            raise NotImplementedError('We are not there yet.')

    def __and__(self, another_male):
        if isinstance(another_male, male.Male):
            newlywed = namedtuple('newlywed', 'husband, wife')
            newlywed.wife = Wife(self.name, self.age, self.children, None)
            newlywed.husband = male.Husband(another_male.name, another_male.age, another_male.children, None)
            newlywed.wife.husband = newlywed.husband
            newlywed.husband.wife = newlywed.wife
            return newlywed
        else:
            raise NotImplementedError('We are not there yet.')


class Mother(parent.Parent, Female):
    def __init__(self, name, age, children):
        parent.Parent.__init__(self, name, age, children)
        Female.__init__(self, name, age)


class Wife(Mother):
    def __init__(self, name, age, children, the_husband):
        Mother.__init__(self, name, age, children)
        if the_husband is None or isinstance(the_husband, male.Husband):
            self.husband = the_husband
        else:
            raise ValueError('Husband must be of a type Husband')

    def __str__(self):
        return f'{Mother.__str__(self)}, Husband: {self.husband.name}'
