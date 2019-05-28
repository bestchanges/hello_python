from human import Human


class Parent(Human):

    def __init__(self, name, age, children):
        Human.__init__(self, name, age)
        self.children = children

    def __str__(self):
        return f'{Human.__str__(self)}, Children: ({[child.__str__() for child in self.children]})'
