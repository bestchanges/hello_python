# Session 8 OOP (Object Oriented Programming)

- inheritance, multiple inheritance
- class methods (not functions)
- getter/setters
- operator overload
- name mangling
- duck typing
- abstract classes

## Screencast
TBD


## Materials
- part "6 Classes" of https://learnxinyminutes.com/docs/python3/
- https://docs.python.org/3/tutorial/classes.html
- [Python OOP Tutorial (youtube, en)](https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) 6 videos * 15min
- abstract classess https://docs.python.org/3/library/abc.html
- https://docs.python.org/3/library/operator.html
- RU https://proglib.io/p/python-oop/, https://proglib.io/p/metaclasses-in-python/


## Project
## The World
There is a world 100x100 cells. 

Each ground call can contain plant on it. 
Plants can:
- grow from seed to mature plant
- give new seeds to nearby free cells
- can be eaten (partially or fully) by herbivore animal 
- die

There are also animals that living on the ground.
Animal can see limit space around it (let say 3 cells).
Animals can perform actions. Each action take specified amount of living power.
Actions:
- walk slowly
- run quickly
- eat (carnivals eat other creatures)
- lookup for partner
- breed (you need male and female that want to breed on nearby cells)
- born some children
- die (when living power goes to zero, or when the time comes)

Make a model of such world. Visualize objects with chars/colors.


Advanced: 
- make several plant types
- plant can suppress other kind of plants nearby slowly killing them