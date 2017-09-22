# Sets

When order and frequency do not matter...

```python
example = set()
dir(example)
example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")
len(example)
example.remove(42) # KeyError if you remove an element not in the set
example.discard(50) # no KeyError
```

```python
example2 = set([28, True, 2.71828, "Helium"])
len(example2) # 4
example2.clear()
len(example2) # 0
```

## Union and Intersection

```python
odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])

odds.union(evens)
evens.union(odds)
odds.intersection(primes)
primes.intersection(odds)
primes.union(composites)
2 in primes # True
6 in odds # False
9 not in evens # True
```
