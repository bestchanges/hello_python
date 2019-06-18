from random import choice
import HumanityGenerator

male_names = ['Johnathan', 'Zaiden', 'Waylon', 'Darien', 'Tyrone', 'Davian', 'Kendrick', 'Augustus', 'Israel', 'Santiago', 'Dylan']
female_names = ['Krista', 'Denise', 'Allison', 'Kaydence', 'Jaslyn', 'Laila', 'Kayleigh', 'Macey', 'Campbell', 'Aiyana', 'Camille', 'Vivian']


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.father = None
        self.mother = None
        self.children = []

    def set_father(self, father):
        if isinstance(father, Human):
            self.father = father

    def set_mother(self, mother):
        if isinstance(mother, Human):
            self.mother = mother

    def add_child(self, child):
        if isinstance(child, Human):
            self.children.append(child)

    def get_older(self, years_count: int):
        self.age += years_count

    def __str__(self):
        return "%s (%s)" % (self.name, ','.join(f"{k}={v}" for k, v in self.get_human_info().items()))

    def get_human_info(self):
        info = {'Age': self.age}
        info.update(self.get_info())
        if len(self.children):
            for index, child in enumerate(self.children, 1):
                info.update({f'Child#{index}': str(child)})
        return info

    def get_info(self):
        return dict()


class Citizen(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.spouse = None

    def get_spouse(self):
        return self.spouse

    def get_married(self, other):
        if isinstance(other, Citizen):
            if self.age < 18 or other.age < 18:
                raise Exception('Citizens cannot be married because one of them is less than 18')
            self.spouse = other
            other.spouse = self
            print(f'{self.name} and {other.name} got married')
            return Family([self, other])

    def get_divorced(self, other):
        if isinstance(other, Citizen):
            self.spouse = None
            other.spouse = None

    def get_info(self):
        info = super().get_info()
        if self.spouse is not None:
            info.update({'Spouse': self.spouse.name})
        return info


class Male(Citizen):
    def __and__(self, other):
        if isinstance(other, Female):
            return self.get_married(other)

    def __mod__(self, other):
        if isinstance(other, Female):
            if not other.pregnant:
                other.pregnant = choice([False, True])
                print(f"{self.name} and {other.name} had sex")
                if other.pregnant:
                    print(f"{other.name} now is pregnant")
        else:
            raise Exception('Two males cannot have sex')

    def get_info(self):
        info = super().get_info()
        info.update({
            'Sex': 'male',
        })
        return info


class Female(Citizen):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.pregnant = False

    def __and__(self, other):
        if isinstance(other, Male):
            return self.get_married(other)

    def __mod__(self, other):
        if isinstance(other, Male):
            if not self.pregnant:
                self.pregnant = choice([False, True])
                print(f"{self.name} and {other.name} had sex")
                if self.pregnant:
                    print(f"{self.name} now is pregnant")
        else:
            raise Exception('Two females cannot have sex')

    def __invert__(self):
        if self.pregnant:
            cls = choice([Male, Female])
            name = choice(male_names) if cls == Male else choice(female_names)
            self.pregnant = False
            child = cls(name, 0)
            child.set_mother(self)
            spouse = self.get_spouse()
            if spouse is not None:
                child.set_father(self.get_spouse())
                spouse.add_child(child)

            self.add_child(child)
            print(f'The child {child.name} was born')

        return self

    def get_info(self):
        info = super().get_info()
        info.update({'Sex': 'female'})
        if self.pregnant:
            info.update({'Pregnant': self.pregnant})
        return info


class Family:
    def __init__(self, members=None):
        self.members = members if members is not None else []

    def add_member(self, member):
        if isinstance(member, Human):
            self.members.append(member)

    def __str__(self):
        info = "\t\t\tFamily: \n"
        for index, member in enumerate(self.members, 1):
            info += f"\t\t\t\tMember {index}: {str(member)}\n"
        return info


if __name__ == '__main__':
    humanity = HumanityGenerator.HumanityGenerator()
    for i in range(50):
        humanity.generate_event()
    print(humanity)
