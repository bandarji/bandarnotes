# Python Notes and Snippets

## Table of Contents

1. Decorators
  * [Time Functions](#time-functions)
1. Dictionaries
  * [Remove Keys](#remove-keys)
1. Numbers
  * [Decimal From Binary](#decimal-from-binary)
1. Printing
  * [ANSI Colors](#ansi-colors)
  * [Pretty Printing](#pretty-printing)
1. [Random Notes](notes.py)

----

## ANSI Colors

```python
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HIGHGREEN = '\033[1;42m'

print(bcolors.HEADER + '####' + bcolors.ENDC)
print(bcolors.HIGHGREEN + 'OK' + bcolors.ENDC)
```

## Decimal From Binary

```python
int('101010101', 2)
```

## Remove Keys

```python
new_dict = {key:d[key] for key in d.keys() - { 'key1', 'key2'}}
```

## Time Functions

```python
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end-start)*1000))
        return result
    return wrapper

@time_it
def calc_cube(numbers):
    return [n*n*n for n in numbers]

cubes = calc_cube(range(100000))
```

## Pretty Printing

```python
from pprint import pprint as pretty

a = [ # ... ]
d = { # ... }
pretty(a)
pretty(d)
```
