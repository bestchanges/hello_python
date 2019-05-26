from female import Mother
from human import Human
from male import Father


class Child(Human):

    def __init__(self, name, age, father, mother):
        Human.__init__(self, name, age)
        if isinstance(father, Father):
            self.father = father
        else:
            raise ValueError('Father must be of a type Father')
        if isinstance(mother, Mother):
            self.mother = mother
        else:
            raise ValueError('Mother must be of a type Mother')

    def __str__(self):
        return f'{Human.__str__(self)}, Father: {self.father.name}, Mother: {self.mother.name}'
