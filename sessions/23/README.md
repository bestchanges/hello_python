# Session 23 Parallel execution - threading
- threading

## Screencast
[![Hello Python Session](http://img.youtube.com/vi/MqXfZSq0nG8/0.jpg)](http://www.youtube.com/watch?v=MqXfZSq0nG8?t=1885 "Hello Python Session")
[![Hello Python Session](http://img.youtube.com/vi/XQ0G25evXuM/0.jpg)](http://www.youtube.com/watch?v=XQ0G25evXuM "Hello Python Session")

## Materials
- [Threading](https://docs.python.org/3/library/threading.html#condition-objects)
  - Condition
  - Semaphore
  - Event
  - Timer
  - Barrier

## Project
У вас есть много (например 1_000_000) веб сайтов доступность которых надо мониторить.
Целевая периодичность проверки одного сайта 1 минута. Время ответа сайта может быть от 1.5 секунд до бесконечности.
Число одновременных проверок ограничено ресурсами машины (скажем 10_000)

Задача: реализовать это используя любые средства модуля Threading 

PS: можно сэмулировать ответы сайтов например с помощью https://github.com/getsentry/responses