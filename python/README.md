# Python Notes and Snippets

## Table of Contents

### Decorators
  * [Time Functions](#time-functions)
### Dictionaries
  * [Remove Keys](#remove-keys)
### HTTP
  * [Read Web Page](#http-get)
  * [Simple Web Server](#http-web-server)
### Numbers
  * [Decimal From Binary](#decimal-from-binary)
  * [Print Leading Zeros](#print-leading-zeros)
### Printing
  * [ANSI Colors](#ansi-colors)
  * [Pretty Printing](#pretty-printing)
  ### Subprocess
  * [Run external command](#subprocess-call)
  * [Run external command (full)](#subprocess-response)
### Tests
  * [File exists?](#file-existence)
  * [Variable exists?](#variable-existence)
  * [Variable iterable?](#variable-iterable)


[Random Notes](notes.py)

## Print Leading Zeros

```python
# '0001'
"1".zfill(4)
"%04d" % 1
"{:>04}".format("1")

```
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

## File Existence

```python
os.path.isfile(filename)
```

## HTTP GET

```python
urllib2.urlopen("http://www.example.com/").read()
```

## HTTP Web Server

```bash
# py v2
$ python -m SimpleHTTPServer 8080
# py v3
$ python -m http.server 8080
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

## Subprocess Call

```python
subprocess.call( ["program", "arg1", "arg2"] )
cmd = "program arg1 arg2"
if cmd: subprocess.call(cmd.split())
```

## Subprocess Response

```python
proc = subprocess.Popen(["ls", "-al"],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
std_input = "/etc/"
out, err = proc.communicate(std_input)
return_code = proc.returncode
```

## Variable Existence

```python
if 'a_var' in locals() or 'a_var' in globals(): print("found")
if hasattr(an_object, 'attribute_name'): print("found")
```

## Variable Iterable

```python
def is_iterable(a_variable):
    try:
        iter(a_variable)
    except TypeError:
        return False
    return True
```
