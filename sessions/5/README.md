# Session 5
- packages: pip, distutils, setuptools
- venv, virtualenv, virtualenvwrapper 
  - shebang
- networking: 
  - sockets
  - HTTP clients. requests, urllib, urllib2
  - asyncio (Not yet!)

## Material
- Python [packaging](https://packaging.python.org/), AND [Glossary](https://packaging.python.org/glossary/)
  - [Installing](https://packaging.python.org/tutorials/installing-packages/):
      - pip https://pip.pypa.io/en/stable/
      - [requirements.txt](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
      - [virtualenv](https://virtualenv.pypa.io/en/stable/)  
      - other tools:
        - deterministic builds: [pipenv](https://pipenv.readthedocs.io/en/latest/) 
        - [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
  - [Creating packages](https://packaging.python.org/tutorials/packaging-projects/) (out of scope)
    - [setuptools](https://setuptools.readthedocs.io/en/latest/)  
    - [distutils](https://packaging.python.org/key_projects/#distutils)
- Shebang `#!/usr/bin/env python3` [stackoverflow](https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take)  
- networking: 
  - sockets [official](https://docs.python.org/3/library/socket.html#example)
  - HTTP clients:
    - [urllib/urllib2](https://docs.python.org/3/library/urllib.html) system module<br> 
      Note The urllib2 module has been split across several modules in Python 3 named urllib.request and urllib.error.
    - Use this: [requests](http://docs.python-requests.org/en/master/user/quickstart/) (and [why](https://stackoverflow.com/questions/2018026/what-are-the-differences-between-the-urllib-urllib2-and-requests-module))
    
     

## Project
GitHub languages popularity

У сервиса github есть мощный API. Задача с помощью этого АПИ выяснить 
на каких языках написаны наиболее ценимые сейчас сообщством проекты.
