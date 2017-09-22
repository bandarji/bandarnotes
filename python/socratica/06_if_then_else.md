# If, Then, Else

```python
input = raw_input("Please enter a test string: ")
if len(input) < 6:
    print("Your string is too short.")
    print("Please enter a string with at least 6 characters.")
```

```python
input = raw_input("Please enter an integer: ")
number = int(input)
if number % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")
```

```python
a = int(raw_input("The length of side a = "))
b = int(raw_input("The length of side b = "))
c = int(raw_input("The length of side c = "))
if a != b and b != c and a != c:
    print("This is a scalene triangle.")
elif a == b and b == c:
    print("This is an equilateral triangle.")
else:
    print("This is an isosceles triangle.")
```
