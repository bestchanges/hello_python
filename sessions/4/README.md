# Session 4
- modules
- `__main__`
- files IO
  - BOM handling encoding 'utf-8-sig'
- JSON data

## Screencast
[![Hello Python Session](http://img.youtube.com/vi/cesOjJRKiDw/0.jpg)](http://www.youtube.com/watch?v=cesOjJRKiDw "Hello Python Session")

## Material
- Official https://docs.python.org/3/tutorial/modules.html#packages
- Rus https://pythoner.name/documentation/tutorial/modules
- modules : https://www.youtube.com/watch?v=CqvZ3vGoGs0
- `__main__` https://www.youtube.com/watch?v=sugvnHA7ElY
- Files https://www.youtube.com/watch?v=Uh2ebFW8OYM
- Files 7.2.1 and Json 7.2.2 https://pythoner.name/documentation/tutorial/output

## Homework tasks
- Read out "PEP 8" https://www.python.org/dev/peps/pep-0008/

## Project
- exchange rate service

Надо написать приложение которое переводит значение из одной валюты в другую.
Пользователь вводит сумму и через пробел валюту, а система выдает эту сумму сконвертированную в дргуие валюты (все, которые она знает).
```
input: 10 USD
output:
643.5 RUR
8.8 EUR
```
задачу написать в два модуля. Первый conv.py - содержит main метод и логику взаимодействия с пользователем, 
второй (например rates.py) содержит методы для вычислений обмена и данные для этого.

В системе введены начальные курсы обмена, 
```
USD/RUR=64.35
BTC/RUR=325960
USD/EUR=0.88
EUR/RUR=72.72
```
Дополнительное задание: 
- позволить пользователю обнволять курсы используя записи вида USD/EUR=value
- сохранять между запусками приложения занчения обменных курсов
