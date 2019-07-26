# Session 21 Parallel execution - GIL 
- threading
- multiprocessing
- GIL

## Screencast
[![Hello Python Session](http://img.youtube.com/vi/NhtmiBbEtsQ/0.jpg)](http://www.youtube.com/watch?v=NhtmiBbEtsQ "Hello Python Session")

## Materials
- https://realpython.com/python-gil/
- https://opensource.com/article/17/4/grok-gil
- [Understanding the Python GIL, David Beazley, 46min, en](https://www.youtube.com/watch?v=Obt-vMVdM8s) (also [graphs](http://www.dabeaz.com/GIL/gilvis/index.html))
- [Python. Многопоточность и GIL, Сергей Лебедев, 1h20m, рус](hhttps://www.youtube.com/watch?v=oa9Tjs80n5E) (GIL starting from 56 min)

## Project
1. test how GIL infer to execution time in different situations
  * incrementing int value many times
  * sleep for fix amount of time
  * filesystem IO
  * network IO
  make a singlethread/multithread/multiprocessess version of each case. Compare their execution time.