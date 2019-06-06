import datetime
import random


class Human:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

        self._marital_status = "single"
        if sex == 'male':
            self._role_title = 'bach'
        else:
            self._role_title = 'bobie'
            self._is_pregnant = False

    @property
    def marital_status(self):
        return self._marital_status

    @property
    def role_title(self):
        return self._role_title

    def full_person_desc(self):
        return self.name + ". " + self._marital_status + ". " + self._role_title

    def __and__(self, other) -> list:
        if self.sex == other.sex:
            raise ValueError('family creation allowed only for different sex persons!')

        created_family_members = [FamilyHuman(self.name, self.age, self.sex, datetime.datetime.now(), other),
                                  FamilyHuman(other.name, other.age, other.sex, datetime.datetime.now(), self)]
        return created_family_members

    def __mod__(self, other) -> str:
        # el sexo
        if self.sex != other.sex:
            if random.randint(1, 101) <= 40:
                if self.sex == 'female':
                    self._is_pregnant = True
                else:
                    other._is_pregnant = True
                return 'got pregnant!'
            else:
                return 'sex without pregnancy'
        else:
            return 'no pregnancy because of same sex'

    def __invert__(self) -> list:
        if self.sex == 'male':
            raise ValueError('male can''t born new baby!')
        if not self._is_pregnant:
            raise ValueError('this female isn''t pregnant!')

        if random.randint(1, 101) <= 50:
            baby_sex = 'male'
        else:
            baby_sex = 'female'

        baby = Human('new_name', 0, baby_sex)

        return [ParentHuman(self.name, self.age, self.sex, [baby]), baby]


class FamilyHuman(Human):

    def __init__(self, name, age, sex, date_of_wedding, spouse: Human, child: Human = None):
        self.date_of_wedding = date_of_wedding
        self.spouse = spouse

        if self.__class__.__name__ == 'FullFamilyHuman':
            super().__init__(name, age, sex, child)
        else:
            super().__init__(name, age, sex)

        if sex == 'male':
            self._marital_status = 'married, has wife ' + spouse.name
            if self._role_title != 'father':
                self._role_title = 'husband'
            else:
                self._role_title = self._role_title + ', husband'
        else:
            self._marital_status = 'married, has husband ' + spouse.name
            if self._role_title != 'mother':
                self._role_title = 'wife'
            else:
                self._role_title = self._role_title + ', wife'

    def __invert__(self) -> list:
        k, baby = Human().__invert__()

        return [FullFamilyHuman(self.name, self.age, self.sex, self.date_of_wedding, self.spouse, [baby]),
                FullFamilyHuman(self.spouse.name, self.spouse.age, self.spouse.sex, self.date_of_wedding, self, [baby]),
                baby]


class ParentHuman(Human):

    children = []

    def __init__(self, name, age, sex, childs: list):
        super().__init__(name, age, sex)

        if sex == 'male':
            self._role_title = 'father'
        else:
            self._role_title = 'mother'

        self.children.extend(childs)

    def all_children(self):
        all_children = ''
        for child in self.children:
            all_children = all_children + child.name + ', '
        return all_children[0:-2:]

    def add_children(self, child: Human):
        self.children.append(child)

    def __and__(self, other) -> list:
        if self.sex == other.sex:
            raise ValueError('family creation allowed only for different sex persons!')

        if isinstance(other, ParentHuman):
            new_family_children = list(set(self.children + other.children))
        else:
            new_family_children = self.children

        created_family_members = [FullFamilyHuman(self.name, self.age, self.sex, datetime.datetime.now(), other, new_family_children),
                                  FullFamilyHuman(other.name, other.age, other.sex, datetime.datetime.now(), self, new_family_children)]
        return created_family_members

    def __invert__(self) -> list:
        k, baby = Human().__invert__()

        self.children.append(baby)

        return [self, baby]


class FullFamilyHuman(FamilyHuman, ParentHuman):

    def __init__(self, name, age, sex, date_of_wedding, spouse: Human, childs: list):
        FamilyHuman.__init__(self, name, age, sex, date_of_wedding, spouse, childs)


if __name__ == '__main__':
    vasya = Human('vasya', 13, 'male')
    klava = Human('klava', 28, 'female')

    print(vasya.full_person_desc())

    kolya = FamilyHuman('kolya', 36, 'male', '2019-02-24', klava)

    print('kolyan marital status is ', kolya.marital_status)
    print(kolya.full_person_desc())

    print(FullFamilyHuman.__mro__)

    mykyta = FullFamilyHuman('mykyta', 45, 'male', '1993-07-14', klava, [vasya])
    print(mykyta.full_person_desc())

    mykyta.add_children(kolya)
    print(mykyta.all_children())

    print('===testing of marriage functionality')

    petya = Human('petro', 23, 'male')
    masha = Human('maria', 21, 'female')

    petya, masha = petya & masha
    print(petya.full_person_desc(), '|', masha.full_person_desc())