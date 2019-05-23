# Session 8 OOP (Object Oriented Programming)

- inheritance, multiple inheritance
- class methods (not functions)
- getter/setters
- operator overload
- name mangling
- duck typing
- abstract classes

## Screencast
[![Hello Python Session](http://img.youtube.com/vi/BFs84FswSY0/0.jpg)](http://www.youtube.com/watch?v=BFs84FswSY0 "Hello Python Session")


## Materials
- part "6 Classes" of https://learnxinyminutes.com/docs/python3/
- https://docs.python.org/3/tutorial/classes.html
- [Python OOP Tutorial (youtube, en)](https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) 6 videos * 15min
- abstract classess https://docs.python.org/3/library/abc.html
- Mixins: [mixins (ru)](http://old.pynsk.ru/posts/2015/Oct/01/interesnye-kontseptsii-mixiny-primesi/#.XNqH03UzZNw), [DictMixin](https://docs.python.org/2/library/userdict.html#UserDict.DictMixin)
- https://docs.python.org/3/library/operator.html
- RU https://proglib.io/p/python-oop/, https://proglib.io/p/metaclasses-in-python/


## Project
## Family
1. Написать классы для обозначения отношений и взаимодействия людей в семье
(с соответствующими свойствами и методами).
Должны быть классы для обозначения человека, отца, матери, мужа, жены, ребенка...

2. Через перегрузку операторов сделать действия:
- male & female => создается семья
- male % female => секс (с вероятностью зачатия ребенка)
- ~ female => рождение ребенка
- ...

делать провреку на допустимость операции, например male & male => должно бросать Exception (в нашем мире =)

3. написать код создание и развития семьи