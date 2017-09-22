# Arithmetic

## Narrower vs Wider Types

* Python results in widest type
* Add an int and a float, and float is wider than int, so the result will be a float

## Python v2

```python
x = 5
y = 5L
long(5)
# 5L
x = 28L # long
y = 28.0 # float
long(3.14) # 3L
x = 1.732
x = 1.732 + 0j
x = complex(1.732)
float(1.732 + 0j) # TypeError exception
```

```python
a = 2
b = 3L
c = 6.0
d = 12 + 0j

a + b # 5L
c - b # 3.0
a * c # 12.0
d / c # (2+0j)
```

```python
16/5 # 3 -- no remainder
16 % 5 # 1 -- the remainder
float(16) / 5 # 3.2
16 / float(5) # 3.2
2 / 0 # ZeroDivisionError exception
```

## Python v3

No more long...
