from child import Child
from male import Male


class Boy(Child, Male):
    def __init__(self, name, age, father, mother):
        Child.__init__(self, name, age, father, mother)
        Male.__init__(self, name, age)
