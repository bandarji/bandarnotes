# Interactive Help

```python
dir() # short for directory
# ['__builtins__', ... ]
dir(__builtins__)
```

```python
help(pow)
pow(2, 10) # same as 2**10
help(hex)
hex(10) # '0xa'
```

## List Available Modules

```python
help('modules')
import math
dir() # now shows 'math'
dir(math)
help(radians) # nope
help(math.radians) # yep
math.radians(180) # returns pi
```
