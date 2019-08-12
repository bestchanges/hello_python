## Table of Contens
- [Unscheduled sessions](#unscheduled-sessions)
- [Backlog](#backlog)


# Unscheduled sessions

## Good console app
- run own console with https://docs.python.org/3/library/readline.html
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
- functools (also with total_ordering())
- dataclasses
- collections.abc
- decimal
- subprocess
- clean code
  - flake8
  - 
- Functional Programming https://docs.python.org/3/howto/functional.html
- Basic structure types 
    - [in 13] sequence types [list, tuple, range](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
    - [in 13] [string is a sequence](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
    - Binary Sequence Types — [bytes, bytearray, memoryview](https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview)
    - Set types [set, frozenset](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
    - Mapping Types — [dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
    - [tutorial](https://docs.python.org/3/tutorial/datastructures.html)
- Container datatypes [collections](https://docs.python.org/3/library/collections.html)
    - defaultdict(int)
    - deque
    - ChainMap
    - Named Tuple
    - OrderedDict 
        - [not redundant even after 3.7](https://stackoverflow.com/questions/50872498/will-ordereddict-become-redundant-in-python-3-7)
    - Counter
- in core library:
    - [heapq](https://docs.python.org/3.0/library/heapq.html)
    - [bisect](https://
    docs.python.org/3.0/library/bisect.html)
    - [array](https://docs.python.org/3.0/library/array.html)
    - [queue](https://docs.python.org/3.0/library/queue.html)
    - [dataclasses](https://docs.python.org/3/library/dataclasses.html)
- External
    - [expiringdict](https://github.com/mailgun/expiringdict)
    - io.StringIO
    - ... what also?
- [decimal calcs](https://docs.python.org/3.7/library/decimal.html)
- [Rounding in Python](https://realpython.com/python-rounding/)
- iterators, generators 
  - also class generators
  - https://wiki.python.org/moin/Generators
  - https://habr.com/ru/post/337314/
  - https://docs.python.org/3/howto/functional.html#passing-values-into-a-generator
- how to name a variable?
- [Python Classes Without Boilerplate](https://github.com/python-attrs/attrs)  
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
  - https://github.com/Rhoynar/python-selenium-bdd
  - https://behave.readthedocs.io/en/latest/
- else statements in loops
- test performance of web-service
- desktop UI (with Tkinter?)
- https://docs.python.org/3/library/csv.html
- overview of https://docs.python.org/3/library/functions.html  
- [breakpoint(), since 3.7](https://docs.python.org/dev/library/functions.html#breakpoint)
- Python 3.8 is coming: https://docs.python.org/3.8/whatsnew/3.8.html
- https://github.com/pyenv/pyenv  
- https://tox.readthedocs.io/en/latest/
- [pipenv, Kenneth Reitz (youtube, 30m)](https://www.youtube.com/watch?v=GBQAKldqgZs)
- [Sanic](https://sanic.readthedocs.io/en/latest/)
- https://www.pygame.org/tags/all
- [Garbage Collection](https://docs.python.org/3/faq/design.html?highlight=garbage%20collect#how-does-python-manage-memory)
- Variables and pointers in Python, [habr](https://habr.com/en/company/mailru/blog/454324/)
- Lots of interresting things in [https://docs.python.org/3/faq/index.html]
- (Learning neural networks within Jupyter Notebook, youtube 1h)[https://www.youtube.com/watch?v=qomCrfctf70&list=PLQTGSfnaYlCuonYGidCFg1aqii9a6cqL4&index=8]

Denis Tomilin:
- Django REST Framework, Django Channels. 
- Отдельно советую ввести в курс дела CGI, WSGI, AG
- Я бы советовал пройти весь development cycle разработки веб-приложения используя стек Python + Django + DRF, с деплойментом и рассказ про опции: разворачивать это дело на хероку, на машинке с gunicorn/uwsgi + nginx, на k8s
- Data Visualization VEGA https://www.youtube.com/watch?v=ms29ZPUKxbU

# Interesting
- [Сколько объектов выделяет Python, выполняя скрипты?](https://habr.com/ru/post/418305/) 
