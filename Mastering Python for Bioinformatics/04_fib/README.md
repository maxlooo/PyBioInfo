# Rabbits and Recurrence Relations

http://rosalind.info/problems/fib/

Write a program called `fib.py` that accepts two positional arguments which are positive integer values describing the number of generations (lte 40) and the size of each litter (gte 5).

The program should print a "usage" statement for `-h` or `--help` flags:

```
$ ./fib.py -h
usage: fib.py [-h] generations litter

Calculate Fibonacci

positional arguments:
  generations  Number of generations
  litter       Size of litter per generation

optional arguments:
  -h, --help   show this help message and exit
```

The output should be the final number of the Fibonacci sequence up to the given generation using the given litter size:

```
$ ./fib.py 5 3
19
```

To test:

```
pytest -xv
```

