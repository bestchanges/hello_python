from female import Female
from child import Child


class Girl(Child, Female):
    def __init__(self, name, age, father, mother):
        Child.__init__(self, name, age, father, mother)
        Female.__init__(self, name, age)
