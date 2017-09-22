# Numbers

## Numbers in Python v2

Python v2 has four types of numbers, while Python v3 has only three.

### Number Types

* int
* long
* float
* complex

#### Integer and Long Integer

```python
a = 28
type(a)
# <type 'int'>
```

```python
import sys
sys.maxint
# 2147483647

b = 2147483647
type(b)
# <type 'int'>
c = b + 1
type(c)
# <type 'long'>
c
# 2147483648L <== see the 'L', for 'long'
print(c)
2147483648 # <== print will not display the 'L'
```

```python
# smallest int
d = -sys.maxint - 1
```

```python
f = 1L      # <== make a long
```

#### Float

```python
e = 2.718281828
```

#### Complex

This is the square route of negative-one (-1). Mathematicians use the letter
'i' to symbolize imaginary numbers. Engineers use 'j', as does Python.

```python
z = 3 + 5.7j
#   3 is the real part
#       5.7j is the imaginary part
type(z)
# <type 'complex'>
z.real
# 3.0
z.imag
# 5.7
```

## Numbers in Python v3

Python v3 dropped 'long' as a number type.
