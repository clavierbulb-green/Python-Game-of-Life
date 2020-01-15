# Game of Life
---

An implementation of Conway's Game of Life in Python.

Written on a whim, to have fun and challenge myself to work out on my own
how to implement the algorithm for the game; to try out generators, nested
functions, type annotation, etc. in Python; and to try to make a fun little
command-line app.

So far, consists only of a generator function that takes a nested list
that represents an initial board of squares as a seed, and yields a list
representing the result of the next round of play.
A value of 1 indicates a 'live' square, whereas a value of 0 a 'dead' square.

Example usage:
```
>>> from life import game_of_life
>>> seed = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
>>> game = game_of_life(seed)
>>> next(game)
[[0, 0, 0], [1, 1, 1], [0, 0, 0]]
>>> next(game)
[[0, 1, 0], [0, 1, 0], [0, 1, 0]]
```
---
### TODO:
- [ ] prettify print output
- [ ] automate (game should run on its own after initial seed is provided)
- [ ] simplify input, allow easy input of larger, more complex seeds
