# Session 22 Parallel execution
- threading
- multiprocessing

## Screencast

## Materials

- [Raymond Hettinger, Thinking about Concurrency, PyCon Russia, 2016](https://www.youtube.com/watch?v=Bv25Dwe84g0)
- [Raymond Hettinger, Keynote on Concurrency, PyBay 2017](https://www.youtube.com/watch?v=9zinZmE3Ogk)


## Project
1. test how GIL infer to execution time in different situations
  * incrementing int value many times
  * sleep for fix amount of time
  * filesystem IO
  * network IO
  * calculating factortial
  make a singlethread/multithread/multiprocessess version of each case. Compare their execution time.