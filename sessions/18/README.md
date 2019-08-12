# Session 17 Code Style (continue)

- PEP-8

## Screencast
[![Hello Python Session](http://img.youtube.com/vi/xM5axEfwCew/0.jpg)](http://www.youtube.com/watch?v=xM5axEfwCew "Hello Python Session")

## Materials

- https://www.python.org/dev/peps/pep-0008/

### Naming
- https://dave.cheney.net/practical-go/presentations/qcon-china.html#_identifiers

Про именование могу сказать, что функции должны быть глаголом. 
Property же идемпотентны и именоваться по существительным. 
Слышал мысль, что слово get_ нужно выкидывать, но это точно не про Python: функции здесь те же объекты, типизация довольно смутная, и поэтому из имени аттрибута класса должно быть понятно, метод это или проперти.

1. function - verb
2. variable - adj.
3. for name for variable to Dict[url, content] use name content_by_url  

### function and method arguments 
Позиционные:
1. Когда аргументы одного типа и их порядок интуитивно понятен. Например, shutil.copy(src, dst)
2. Когда порядок аргументов не важен. Например, sum(1, 2, 3)
3. Когда аргументы одного типа и одного назначения. Например, pyrsistent.PList(1, 2, 3)
4. Когда аргумент один, и его назначение понятно. Например, register(user). А вот так плохо: user.register(True), потому что непонятно, что это за True.

В остальных случаях всегда лучше передавать ключевые аргументы. Соответственно, в сигнатуре указывать их как keyword-only, чтобы об этом не забывать.

## Project
Создать правила по наименованию переменных для разных случаев.
Примеры (не ограничаиваться ими!):
- sequence of objects
- dict, key = name, value = some object or named tuple
- int
- set of strings
- list of complicated structure of data
