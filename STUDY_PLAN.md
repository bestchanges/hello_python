## Table of Contens
- [Sessions](#sessions)
- [Unscheduled sessions](#unscheduled-sessions)
- [Backlog](#backlog)

# Sessions
## [Session 1](sessions/1/)
- intro: projects, zen, code_style
- install & setup (PyCharm)
- run, debug, python console
- types (numbers, strings, bool)
- read/write stdin/stdout
- variables
- control flow (if, for, while)
+ projects: guess_game

## [Session 2](sessions/2/)
- complex types (tuple, array, dict, set)
- iterables, with statement (need to repeat)
- exceptions
+ projects/kalimbas

## [Session 3](sessions/3/)
- functions
- lambda-functions 
- generators 
+ projects/happy_tickets
+ projects/prime_numbers
+ projects/gallow_game

## [Session 4](sessions/4/)
- modules
- `__main__`
- files IO
  - BOM handling encoding 'utf-8-sig'
- JSON data
- project:  exchange rate service

## [Session 5](sessions/5/)
- packages: pip, distutils, setuptools
- venv, virtualenv, virtualenvwrapper 
- networking: 
  - sockets
  - HTTP clients. requests, urllib, urllib2
  - asyncio (not yet)
- project: GitHub languages popularity

## [Session 6](sessions/6/) RESTful backend
- Flask
  - routes
  - endpoints
  - dev mode server
- project: todolist backend 
- decorators
  - project: cache function result with decorator

## [Session 7](sessions/7/) Test Driven Development
- Test Driven Development
- PyTest
- WebSockets

Project
- write WebSockets based chat using TDD

## [Session 8](sessions/8/) 

## Python Basics (continue) 
- variables scope https://www.youtube.com/watch?v=QVdf0LgmICw 
- Decorators with arguments: https://www.youtube.com/watch?v=KlBPCzcQNU8
- free variables
  - closures https://www.youtube.com/watch?v=swU3c34d2NQ
- sorting https://www.youtube.com/watch?v=D3JvDWO-BY4
- iterators, generators 
  - also class generators
  - https://wiki.python.org/moin/Generators
  - https://habr.com/ru/post/337314/
- context managers (with statement) https://docs.python.org/3/reference/compound_stmts.html#the-with-statement


# Unscheduled sessions

## 8 Python Basics (continue) 
- variables scope https://www.youtube.com/watch?v=QVdf0LgmICw 
- Decorators with arguments: https://www.youtube.com/watch?v=KlBPCzcQNU8
- free variables
  - closures https://www.youtube.com/watch?v=swU3c34d2NQ
- sorting https://www.youtube.com/watch?v=D3JvDWO-BY4
- iterators, generators 
  - also class generators
  - https://wiki.python.org/moin/Generators
  - https://habr.com/ru/post/337314/
- context managers (with statement) https://docs.python.org/3/reference/compound_stmts.html#the-with-statement


## Good console app
- run own console with https://docs.python.org/3/library/readline.html
- read CLI args
- logging

- project: command line currency converter (from session 4)  
  - available commands generated on fly from object
  - support of command line options
  - command line usage with exit after completion
  - help function displays docstring 
  - autocomplete command in console
  - exit Ctrl+D
  
## Unittests
- unittest
- assert
- mocking: functions, files, etc.
- coverage
  - https://coverage.readthedocs.io/en/coverage-4.2/index.html
- docstrings
- doc generation

## AsyncIO
- coroutines https://docs.python.org/3/reference/compound_stmts.html#coroutines
- [Debug asyncio in PyCharm](https://youtu.be/9x9xIR9tFlc)

## Object Oriented Programming
- OOP, classes https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
  - inheritance
  - class methods (not functions) 
  - getter/setters https://www.youtube.com/watch?v=jCzT9XFZ5bw
  - [name mangling](https://dbader.org/blog/meaning-of-underscores-in-python) - Refer to part about `__var`
- duck typing

## Parallel execution 
- threading 
- multiprocessing
- GIL 
  - https://opensource.com/article/17/4/grok-gil

## Python modules overview 
- itertools https://docs.python.org/3.7/library/itertools.html
- collections https://docs.python.org/3/library/collections.html
- defaultdict() https://docs.quantifiedcode.com/python-anti-patterns/correctness/not_using_defaultdict.html
- datetime

## Flask (continue)
- flask: data storage
  - SQL Databases
  - noSQL databases
- flask: user management, auth, login, password reset
- flask: templates
- flask: production app server

## RESTful API
- swagger tools
  - https://swagger.io/tools/swagger-editor/
  - https://swagger.io/tools/swagger-inspector/
  - https://swagger.io/tools/swagger-codegen/
  - https://swagger.io/tools/swagger-ui/
  - [PyCharm plugin](https://plugins.jetbrains.com/plugin/8347-swagger)
- flask 
  - https://github.com/flask-restful/flask-restful
  - https://github.com/noirbizarre/flask-restplus
  - https://github.com/rochacbruno/flasgger
- django
  - https://github.com/marcgibbons/django-rest-swagger
  - https://www.django-rest-framework.org/topics/documenting-your-api/
- aiohttp
  - https://docs.aiohttp.org/en/stable/third_party.html
  - https://github.com/maximdanilchenko/aiohttp-apispec
  - https://github.com/cr0hn/aiohttp-swagger


## jupyter notebooks
- jupyter notebook 
- jupyterhub 
- jupyterlab 
- [realtime co-editing](https://www.youtube.com/watch?v=dSjvK-Z3o3U&feature=youtu.be&t=1013)
- https://proglib.io/p/jupyter/
- [JupytherHub in Yandex](https://www.youtube.com/watch?v=I49jOFSCV00&feature=youtu.be&t=211)
- https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks 

## aiohttp
- presentations by Svetlov
- https://docs.aiohttp.org/en/stable/third_party.html

# Backlog

- data model https://docs.python.org/3/reference/datamodel.html
  - magic methods https://docs.python.org/3/reference/datamodel.html#special-method-names
- execution model https://docs.python.org/3/reference/executionmodel.html
- publish package with setuptools
- type hints https://www.python.org/dev/peps/pep-0484/
- docker+python
- docker-compose
- queues
  - rabbitmq
  - nameko
- QA automation
- test performance of web-service
- Django web site
- desktop UI (with Tkinter?)
- ML
- clean code: codestyle
  - https://landscape.io/#
  - https://www.python.org/dev/peps/pep-0008/
  - pycodestyle

# Backlog projects
+ trading bot
+ todoist_automation
+ currency_exchange_rates
+ gimblet_online_game
+ object recognition
+ smart home gadgets
+ chat bot (telegram, alice, skype)
