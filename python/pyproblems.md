Common Python Programming Issues
================================

Save yourself hours of debugging and steer clear from causing production issues
with your code.

# Table of Contents

1. Construct a [list of lists](#list-of-lists)

# List of Lists

When you want `[[], [], [], [],... []]`, you might want to use code for list
initialization. Let us construct a ten-element list, with an empty list as each
element. Then, let's add a value to one of the inner lists. Afterward, we shall
inspect the outer list.

## Method One

```python
a1 = []
for _ in range(10):
    a1.append([])
print(a1) # [[], [], [], [], [], [], [], [], [], []]
a1[1].append(1)
print(a1) # [[], [1], [], [], [], [], [], [], [], []]
```

Okay, this worked as expected. It does not require many lines of code. I do not
consider it ugly. However, code shortcuts exist.

## Method Two

```python
a2 = [[]] * 10
print(a2) # [[], [], [], [], [], [], [], [], [], []]
a2[2].append(2)
print(a2) # [[2], [2], [2], [2], [2], [2], [2], [2], [2], [2]]
```

The problem here: ten elements point to the same reference (memory address).

```
>>> a = [[]] * 10
>>> for e in a: print(id(e))
... 
4372187184
4372187184
4372187184
4372187184
4372187184
4372187184
4372187184
4372187184
4372187184
4372187184
```

## Method Three

```python
a3 = [[] for _ in range(10)]
print(a3) # [[], [], [], [], [], [], [], [], [], []]
a3[3].append(3)
print(a3) # [[], [], [], [3], [], [], [], [], [], []]
```

We now have a list of lists initialization where the outer list does not contain
elements referencing the same memory location.

```
>>> a = [[] for _ in range(10)]
>>> for e in a: print(id(e))
... 
4342596024
4342595952
4342596096
4342596168
4342596312
4342596384
4342596456
4342596528
4342596600
4342596672
```
