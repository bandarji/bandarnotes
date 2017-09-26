# Lists

```python
example = list()
example = []

primes = [2, 3, 5, 7, 11, 13]
primes.append(17)
primes.append(19)

primes
# [2, 3, 5, 7, 11, 13, 17, 19]
primes[0]
# 2
primes[1]
# 3
primes[5]
# 5
primes[-1]
# 19
primes[-2]
# 17
primes[-9]
# Only wrap once -- IndexError
```

## Slices

```python
primes[2:5]
# [5, 7, 11]
primes[0:6]
[2, 3, 5, 7, 11, 13]
```

## Mixed Types

```python
example = [128, True, "Alpha", 1.732, [64, False]]
```

## Duplicate Entries

```python
rolls = [4, 7, 2, 7, 12, 4, 7]
```

## Combine Lists

```python
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
numbers + letters
# [1, 2, 3, 'a', 'b', 'c']
letters + numbers
# ['a', 'b', 'c', 1, 2, 3]
```
