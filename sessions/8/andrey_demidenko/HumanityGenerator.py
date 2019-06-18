from random import choice, randint
from main import Human, Male, Female, male_names, female_names


class HumanityGenerator:
    def __init__(self):
        self.singles = []
        self.families = []

    def __iter__(self):
        return self

    def generate_population(self, quantity):
        for index in range(quantity):
            self.singles.append(HumanityGenerator.generate_single())

    @staticmethod
    def generate_single() -> Human:
        cls = choice([Male, Female])
        name = choice(male_names) if cls == Male else choice(female_names)
        age = randint(5, 35)
        return cls(name, age)

    def generate_family(self):
        man = None
        woman = None
        while True:
            for index, single in enumerate(self.singles):
                if man is None and isinstance(single, Male) and single.age >= 18:
                    man = single
                    del self.singles[index]
                if woman is None and isinstance(single, Female) and single.age >= 18:
                    woman = single
                    del self.singles[index]
            if man is not None and woman is not None:
                self.families.append(man & woman)
                print(f"New family is generated. Husband {man.name} and wife {woman.name}")
                break
            self.singles.append(HumanityGenerator.generate_single())

    @staticmethod
    def pass_years(humans, years_count: int):
        for human in humans:
            human.get_older(years_count)
            if len(human.children):
                HumanityGenerator.pass_years(human.children, years_count)

    def generate_event(self):
        event = randint(1, 5)
        """Generate family"""
        if event == 1:
            self.generate_family()

        """Pass years through the families and singles"""
        if event == 2:
            years = randint(1, 5)
            HumanityGenerator.pass_years(self.singles, years)
            for family in self.families:
                HumanityGenerator.pass_years(family.members, years)
            print(F'Pass {years} years')

        """Try Random children to get married"""
        if event == 3:
            boy = None
            girl = None
            for family in self.families:
                for member in family.members:
                    for child in member.children:
                        if child.age >= 18 and child.get_spouse() is None:
                            if isinstance(child, Male):
                                boy = child
                            else:
                                girl = child
            if boy and girl:
                self.families.append(boy & girl)

        """Having a sex"""
        if event == 4:
            if len(self.families):
                family = self.families[randint(0, len(self.families) - 1)]
                man = None
                woman = None
                for member in family.members:
                    if isinstance(member, Male):
                        man = member
                    else:
                        woman = member
                if man is not None and woman is not None:
                    man % woman

        """Trying to born baby"""
        if event == 5:
            for family in self.families:
                for woman in [member for member in family.members if isinstance(member, Female)]:
                    if woman.pregnant:
                        ~woman

    def __str__(self):
        info = "Humanity: \n"
        if len(self.singles):
            info += "\t\tSingles: \n"
            for single in self.singles:
                info += f"\t\t\t{str(single)} \n"
        if len(self.families):
            info += "\t\tFamilies: \n"
            for family in self.families:
                info += str(family)
        return info
