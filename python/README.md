# Python Notes and Snippets

## Table of Contents

### Debugging
  * [Python Debugger](#python-debugger)
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
  * [Roll Die](#roll-die)
### Printing
  * [ANSI Colors](#ansi-colors)
  * [Pretty Printing](#pretty-printing)
  * [Wrapping Text](#wrapping-text)
### Sorting
  * [Unique elements in order of encounter](#unique-element-sort)
### Strings
  * [Multiple finds](#multiple-finds)
### Subprocess
  * [Run external command](#subprocess-call)
  * [Run external command (full)](#subprocess-response)
### Tests
  * [File exists?](#file-existence)
  * [Variable exists?](#variable-existence)
  * [Variable iterable?](#variable-iterable)

* [Random Notes](notes.py)
* [Terminal Tables](terminal_tables.md)

## Python Debugger

```python
import pdb; pdb.set_trace()
'''
h # help
s # step
n # next
unt # until
r # return
c # continue
j LINE # jump to line number without executing
l # list source code
p EXPR # eval expression
'''
```

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

## Multiple Finds

```python
char_list = ':/|'
if any(c in char_list for c in test_string):
    do()

pattern = re.compile(r'[:/|]')
if pattern.search(test_string):
    do()

all(x in [str1, str2, str3] for x in [':', '/', '|'])
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

## Roll Die

```python
from random import random
roll_die = lambda sides: int(random() * sides) + 1
roll_die(6)
roll_die(20)
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

## Unique Element Sort

```python
s = 'yellowwood door reeffecting'
print(sorted(set(s), key=s.index))
# ['y', 'e', 'l', 'o', 'w', 'd', ' ', 'r', 'f', 'c', 't', 'i', 'n', 'g']
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

## Wrapping Text

```python
long_ass_string = "Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit amet consectetur adipisci[ng] velit, sed quia non-numquam [do] eius modi tempora inci[di]dunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur"
    print("\n".join(textwrap.wrap(long_ass_string, width=60)))
```
