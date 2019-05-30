## Table of Contens
- [Unscheduled sessions](#unscheduled-sessions)
- [Backlog](#backlog)


# Unscheduled sessions

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
- iterators, generators 
  - also class generators
  - https://wiki.python.org/moin/Generators
  - https://habr.com/ru/post/337314/
  - https://docs.python.org/3/howto/functional.html#passing-values-into-a-generator
- Decorators
    - closures https://www.youtube.com/watch?v=swU3c34d2NQ
    - Decorators with arguments: https://www.youtube.com/watch?v=KlBPCzcQNU8

- asyncio continue
  - Exceptions handling
  - sync-async code marriage
- data manipulation
  - [copy](https://docs.python.org/3.0/library/copy.html)
  - sorting https://www.youtube.com/watch?v=D3JvDWO-BY4
  - caching with [weakref](https://docs.python.org/3.0/library/weakref.html)
  - [itertools](https://docs.python.org/3.7/library/itertools.html)
- GUI with Tk
  - https://docs.python.org/3.0/library/tk.html
- Internationalization
  - https://docs.python.org/3.0/library/i18n.html  
- scheduled execution [sched](https://docs.python.org/3.0/library/sched.html)
- repr vs str
  - https://docs.python.org/3.0/library/reprlib.html
- HTTP load tests [Asyncio/Aiohttp — предел производительности](https://www.youtube.com/watch?v=ctLi6_mrPLc) youtube, ru, 20m
- functional programming https://docs.python.org/3/howto/functional.html
- defaultdict() https://docs.quantifiedcode.com/python-anti-patterns/correctness/not_using_defaultdict.html
- datetime
- inspect, tokenize
- math, statistics
- os, pathlib
- requests (with Session)
- shutil
- tkinter
- data model https://docs.python.org/3/reference/datamodel.html
  - magic methods https://docs.python.org/3/reference/datamodel.html#special-method-names
- execution model https://docs.python.org/3/reference/executionmodel.html
- create packages distributions
  - publish package with setuptools
- type hints 
  - https://docs.python.org/3/library/typing.html
  - https://www.python.org/dev/peps/pep-0484/
- docker+python
- docker-compose
- queues
  - rabbitmq
  - nameko
- QA automation
- else statements in loops
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
- [Sanic](https://sanic.readthedocs.io/en/latest/)
- https://www.pygame.org/tags/all

Denis Tomilin:
- Django REST Framework, Django Channels. 
- Отдельно советую ввести в курс дела CGI, WSGI, AG
- Я бы советовал пройти весь development cycle разработки веб-приложения используя стек Python + Django + DRF, с деплойментом и рассказ про опции: разворачивать это дело на хероку, на машинке с gunicorn/uwsgi + nginx, на k8s
- Data Visualization VEGA https://www.youtube.com/watch?v=ms29ZPUKxbU

# Backlog projects
+ [Python Face Recognition Tutorial](https://www.youtube.com/watch?v=QSTnwsZj2yc), youtube, en, 30m - контент так себе, а вот библиотеку надо попробовать
+ trading bot
+ todoist_automation
+ currency_exchange_rates
+ gimblet_online_game
+ object recognition
+ smart home gadgets
+ chat bot (telegram, alice, skype)
- https://www.home-assistant.io/