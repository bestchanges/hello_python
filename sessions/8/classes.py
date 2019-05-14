class Parent:
    def __init__(self):
        print('parent')
        self._private = "I'm parent private"

    def sayParent(self):
        print(self._private)


class Child(Parent):
    classAttr = 123

    def __init__(self):
        super().__init__()
        self._private = "I'm child private"
        print('child')

    def sayChild(self):
        print(self._private)

c = Child()
c.new_attr = 123
print(dir(c))
c.sayChild()
c.sayParent()
assert isinstance(c, Parent)
assert isinstance(c, Child)
