# Unit Tests

There are two types of engineers. The first writes code, then walks away and
does not watch it run. Then, there's the second type, those who write unit
tests.

## Manually Testing Area of a Circle Function

Engineer writes a simple function to provide the area of a circle.

```python
from math import pi
def circle_area(r):
    return pi*(r**2)
```

Testing provides unexpected output.

```python
radii = [2, 0, -3, 2 + 5j, True, "radius"]
message = "Area of circle of radius {radius} is {area} square units."
for r in radii:
    a = circle_area(r)
    print(message.format(radius=r, area=a))
```

Running shows area for negative radius measurement and accepts a string.

## Unit Testing Function

For `circles.py`, create either `test_circles.py` or `circles_test.py`, or in
a separate folder.

```python
import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1), pi) # assertAlmostEqual 7-decimal
        self.assertAlmostEqual(circle_area(0), 0)  # places accuracy
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)
```

Run tests.

```bash
python -m unittest test_circles
python -m unittest # runs all tests found
```

This runs clean. Now, let's add tests for invalid input.

```python
import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1), pi) # assertAlmostEqual 7-decimal
        self.assertAlmostEqual(circle_area(0), 0)  # places accuracy
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def test_values(self):
        # Expect a ValueError exception when passing in a negative radius
        self.assertRaises(ValueError, circle_area, -2)
```

This fails because we need to add the `ValueError` exception to the original
function.

```python
from math import pi
def circle_area(r):
    if r < 0:
        raise ValueError("The radius cannot be negative.")
    return pi*(r**2)
```

Unit tests now pass. Use `help(unittest.TestCase.assertSetEqual)` for help on an
assertion type.

Let's add more tests.

```python
import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1), pi) # assertAlmostEqual 7-decimal
        self.assertAlmostEqual(circle_area(0), 0)  # places accuracy
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def test_values(self):
        # Expect a ValueError exception when passing in a negative radius
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")
```

Again, we must account for these in the original function.

```python
from math import pi
def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number.")
    if r < 0:
        raise ValueError("The radius cannot be negative.")
    return pi*(r**2)
```
