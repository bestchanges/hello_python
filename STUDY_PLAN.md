## Table of Contens
- [Sessions](#sessions)
- [Unscheduled sessions](#unscheduled-sessions)
- [Backlog](#backlog)



# Unscheduled sessions

## Python Basics (continue) 
- variables scope 
  - https://www.youtube.com/watch?v=QVdf0LgmICw 
  - [Introduction to namespaces and scopes](https://nbviewer.jupyter.org/github/rasbt/python_reference/blob/master/tutorials/scope_resolution_legb_rule.ipynb#introduction)
  - https://www.programiz.com/python-programming/namespace
- Decorators with arguments: https://www.youtube.com/watch?v=KlBPCzcQNU8
- free variables
  - closures https://www.youtube.com/watch?v=swU3c34d2NQ
- sorting https://www.youtube.com/watch?v=D3JvDWO-BY4
- iterators, generators 
  - also class generators
  - https://wiki.python.org/moin/Generators
  - https://habr.com/ru/post/337314/
  - https://docs.python.org/3/howto/functional.html#passing-values-into-a-generator
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

## Parallel execution 
- threading 
- multiprocessing
- GIL 
  - https://opensource.com/article/17/4/grok-gil

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


## Python bytecode
  - https://opensource.com/article/18/4/introduction-python-bytecode
  - https://docs.python.org/3/library/dis.html


# Backlog

- collections https://docs.python.org/3/library/collections.html
  - defaultdict(int)
  - deque
  - OrderedDict - every dict sinse 3.7
  - Counter
- HTTP load tests [Asyncio/Aiohttp — предел производительности](https://www.youtube.com/watch?v=ctLi6_mrPLc) youtube, ru, 20m
- functional programming https://docs.python.org/3/howto/functional.html
- itertools https://docs.python.org/3.7/library/itertools.html
- defaultdict() https://docs.quantifiedcode.com/python-anti-patterns/correctness/not_using_defaultdict.html
- datetime
- inspect, tokenize
- math, statistics
- os, pathlib
- shutil
- tkinter
- data model https://docs.python.org/3/reference/datamodel.html
  - magic methods https://docs.python.org/3/reference/datamodel.html#special-method-names
- execution model https://docs.python.org/3/reference/executionmodel.html
- create packages distributions
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
- [breakpoint(), since 3.7](https://docs.python.org/dev/library/functions.html#breakpoint)
- https://github.com/pyenv/pyenv  
- https://tox.readthedocs.io/en/latest/
- [pipenv, Kenneth Reitz (youtube, 30m)](https://www.youtube.com/watch?v=GBQAKldqgZs)
- Sanic
Denis Tomilin:
- Django REST Framework, Django Channels. 
- Отдельно советую ввести в курс дела CGI, WSGI, AG
- Я бы советовал пройти весь development cycle разработки веб-приложения используя стек Python + Django + DRF, с деплойментом и рассказ про опции: разворачивать это дело на хероку, на машинке с gunicorn/uwsgi + nginx, на k8s
- Data Visualization VEGA https://www.youtube.com/watch?v=ms29ZPUKxbU

# Backlog projects
+ trading bot
+ todoist_automation
+ currency_exchange_rates
+ gimblet_online_game
+ object recognition
+ smart home gadgets
+ chat bot (telegram, alice, skype)
- https://www.home-assistant.io/