# Game of Life
---

An implementation of Conway's Game of Life in Python.

Written on a whim, to have fun and challenge myself to work out on my own
how to implement the algorithm for the game; to try out generators, nested
functions, type annotation, etc. in Python; and to try to make a fun little
command-line app.

The program can read its input from a .csv file containing the starting seed
configuration. A value of 1 indicates a 'live' square,whereas a value of 0
indicates a 'dead' square. The program then prints the state of the board as
its cells 'evolve'.

```
usage: life.py [-h] [-f]

optional arguments:
  -h, --help    show this help message and exit
  -f , --file   file to read game seed from
```

Example:
```
python3 life.py -f samples/blinker.csv
```

or:
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
  - [ ] center board
  - [ ] add color to make live cells stand out
- [x] automate (game should run on its own after initial seed is provided)
- [ ] allow saving output to a file
- [ ] allow reading input from an image, other formats, etc.
- [ ] allow user to control number of iterations to run through
- [ ] simplify input, allow easy input of larger, more complex seeds

---
### REFERENCE:
- [Conway's Game of Life - Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
-
- [Reading and Writing CSV Files in Python – Real Python](https://realpython.com/python-csv/)
- [csv — CSV File Reading and Writing — Python 3.8.1 documentation](https://docs.python.org/3/library/csv.html)
- [Argparse Tutorial — Python 3.8.1 documentation](https://docs.python.org/3/howto/argparse.html#id1)
- [argparse — Parser for command-line options, arguments and sub-commands — Python 3.8.1 documentation](https://docs.python.org/3/library/argparse.html#const)
- [Curses Programming with Python — Python 3.8.1 documentation](https://docs.python.org/3/howto/curses.html)
- [curses — Terminal handling for character-cell displays — Python 3.8.1 documentation](https://docs.python.org/3/library/curses.html#curses.wrapper)

- [python - Output to the same line overwriting previous - Stack Overflow](https://stackoverflow.com/questions/26584003/output-to-the-same-line-overwriting-previous/26584483)
- [printing a two dimensional array in python - Stack Overflow](https://stackoverflow.com/questions/17870612/printing-a-two-dimensional-array-in-python)
- [How to create a number of empty nested lists in python - Stack Overflow](https://stackoverflow.com/questions/19249201/how-to-create-a-number-of-empty-nested-lists-in-python)
- [python - Don't show long options twice in print_help() from argparse - Stack Overflow](https://stackoverflow.com/questions/18275023/dont-show-long-options-twice-in-print-help-from-argparse)
