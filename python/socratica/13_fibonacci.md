# Recursion, the Fibonacci Sequence and Memoization

* The Fibonacci Sequence starts with [1, 1, 2, 3, 5, 8, 13, 21].
* Each term is the sum of the prior two terms.
* Write a function to return the n-th value in the sequence.

```python
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 11):
    print(n, ":", fibonacci(n))

for n in range(1, 101):
    print(n, ":", fibonacci(n)) # Takes too long to calculate
```


## Memoization

Store a calculated value for later use.

```python
fibonacci_cache = {}

def fibonacci(n):
    # If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

for n in range(1, 1001):
    print(n, ":", fibonacci(n))
```

### More Elegant Method

```python
# Get the Least Recently Used Cache function
from functools import lru_cache

@Lru_cache(maxsize = 1000) # default is 128 entries
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 501):
    print(n, ":", fibonacci(n))
```

## Argument Checking

```python
# Get the Least Recently Used Cache function
from functools import lru_cache

@Lru_cache(maxsize = 1000) # default is 128 entries
def fibonacci(n):
    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    # Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 501):
    print(n, ":", fibonacci(n))
```

## Ratio Between Consequetive Terms

```python
for n in range(1, 51):
    print(fibonacci(n+1) / fibonacci(n)) # 1.618033988749895, Golden Ratio
```
