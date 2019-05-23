from abc import ABC, abstractmethod


class P(ABC):
    @abstractmethod
    def abst(self):
        print('abst parent')

    def __mul__ (self, other):
        return 'always'


class C(P):
    def abst(self):
        super().abst()

c1 = C()
c1.abst()