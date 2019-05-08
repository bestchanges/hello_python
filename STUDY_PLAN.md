# Study Plan

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

## [Session 6](sessions/6/)
# Session 6 RESTful backend
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

# Unscheduled sessions

## Good console app
- 123
- run own console with https://docs.python.org/3/library/readline.html
- read CLI args
- logging

- project: command line currency converter (from session 4)  
  - support of command line options
  - command line usage with exit after completion 
  - autocomplete command in console
  - exit Ctrl+D
  
## Unittests
- unittest
- assert
- mocking: functions, files, etc.
- coverage
- docstrings
- doc generation

## AsyncIO
- closures https://www.youtube.com/watch?v=swU3c34d2NQ
- [Debug asyncio in PyCharm](https://youtu.be/9x9xIR9tFlc)

## Object Oriented Programming
- classes, OOP, duck typing
  - getter/setters https://www.youtube.com/watch?v=jCzT9XFZ5bw 

## Parallel execution 
- threading, multiprocessing
- GIL 
  - https://opensource.com/article/17/4/grok-gil

## Python Basics 
- variables scope https://www.youtube.com/watch?v=QVdf0LgmICw 
- Decorators with arguments: https://www.youtube.com/watch?v=KlBPCzcQNU8
- free variables
- sorting https://www.youtube.com/watch?v=D3JvDWO-BY4
- iterators, generators 
  - also class generators
  - https://wiki.python.org/moin/Generators
  - https://habr.com/ru/post/337314/
- context managers (with)


## Python modules overview 
- itertools https://docs.python.org/3.7/library/itertools.html
- collections https://docs.python.org/3/library/collections.html
- defaultdict() https://docs.quantifiedcode.com/python-anti-patterns/correctness/not_using_defaultdict.html
- datetime

## Flask continue
- flask: data storage
  - SQL Databases
  - noSQL databases
- flask: user management, auth, login, password reset
- flask: templates
- flask: production app server


# Backlog

- publish package with setuptools
- type hints https://www.python.org/dev/peps/pep-0484/
- magic methods
- docker
- jupyter notebooks
- queues: rabbitmq
- QA automation
- test performance of web-service
- Django web site
- desktop UI (with Tkinter?)
- Django
- acyncio
- ML


# Backlog projects
+ github_languages_popularity
+ todoist_automation
+ currency_exchange_rates
+ chat_service
+ gimblet_online_game
+ object recognition
+ smart home gadgets
+ telegram bot
