# Functions

```python
dir()
def f():
    pass
f() # does nothing -- good job
f # <function f at 0x...>
dir() # now 'f' shows up
```

```python
def ping():
    return "Ping!"
ping()
x = ping()
print(x)
```

## Required Arguments

### Require One Argument

```python
import math
def volume(r):
    """Returns sphere volume with radius 'r'."""
    v = (4.0/3.0) * math.pi * r**3
    return v
```

### Require Two Arguments

```python
def triangle_area(b, h):
    """Return area of a triangle with base 'b' and height 'h'."""
    return 0.5 * b * h
```

## Keyword Arguments

```python
def cm(feet = 0, inches = 0):
    """Converts length from feet and inches to centimeters."""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm
cm(feet=5)
cm(inches=70)
cm(feet=5, inches=8)
```

## Mixing Arguments

* Required arguments come before keyword arguments or SyntaxError exception
