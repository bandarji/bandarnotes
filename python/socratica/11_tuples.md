# Tuples

Tuples store ordered data, similar to a list.

```python
prime_numbers = [2, 3, 5, 7, 11, 13, 17]
perfect_squares = (1, 4, 9, 16, 25, 36)
print("# Primes = ", len(prime_numbers))
print("# Sqares = ", len(perfect_squares))
for p in prime_numbers: print("Prime: ", p)
for n in perfect_squares: print("Square: ", n)
```

## Difference Between List and Tuples

* Lists have more functions available, but at a cost
* Change list data (add, remove, update)
* Tuples are immutable

```python
print(dir(prime_numbers))
print(80*"-")
print(dir(perfect_squares))
```

```python
import sys
list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)
print("List size = ", sys.getsizeof(list_eg))
print("Tuple size = ", sys.getsizeof(tuple_eg))
# 68 vs 60
```

### Tuples: Faster Than Lists

```python
import timeit
list_test = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)
print("List time: ", list_test)
print("Tuple time: ", tuple_test)
# 0.1049 vs 0.0143
```

## Working With Tuples

```python
empty_tuple = ()
test1 = ("a")
test2 = ("a", "b")
test3 = ("a", "b", "c")

print(empty_tuple)   # ()
print(test1)         # a <== change to test1 = ("a",) to really make a tuple
                     # Single-element tuple makes no sense
print(test2)         # ('a', 'b')
print(test3)         # ('a', 'b', 'c')
```

```python
test1 = 1,
test2 = 1, 2
test3 = 1, 2, 3
```

## Variable Assignment From Tuple

### Method One

```python
# (age, country, knows_python)
survey = (27, "Vietnam", True)
age = survey[0]
country = survey[1]
knows_python = survey[2]
print("Age = ", age)
print("Country = ", country)
print("Knows Python? ", knows_python)
```

### Method Two

```python
survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2
print("Age = ", age)
print("Country = ", country)
print("Knows Python? ", knows_python)
```

## Single-Element Tuple

```python
country = ("Australia")
print(country)
# Australia
country = ("Australia",)
print(country)
# ('Australia',)
```

## Unpack Errors

```python
x, y, z = (1, 2)
# ValueError exception
```
