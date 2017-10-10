# Sorting

## Basic / Default Sort (Alphabetical and Value Order)

```python
# Alkaline earth metals
# sorted by atomic number
earth_metals = [
    "Beryllium",
    "Magnesium",
    "Calcium",
    "Strontium",
    "Barium",
    "Radium"
]
earth_metals.sort() # alphabetic order, by default
earth_metals
['Barium', ..., 'Strontium']
```

## Reverse Alphabetical and Value Order Sort

```python
earth_metals.sort(reverse=True)
```

## Sort Function Not Available For Sets

```python
earth_metals = set(earth_metals)
earth_metals.sort()
AttributeError: 'tuple' object has no attribute 'sort'
```

Remember, sets are immutable (unchangeable).

## Sort By Key

The ```sort()``` function for lists accepts a ```key``` argument. The argument
allows passing a function for identifying how to order the sort.

### Solar System's Planets

Tuples for each planet contain the following fields: name, equator radius in 
kilometers, average density (g/cm^3) and AU distance to the Sun.

```python
planets = [
    ("Mercury", 2440, 5.43, 0.395),
    ("Venus", 6052, 5.24, 0.723),
    ("Earth", 6378, 5.52, 1.000),
    ("Mars", 3396, 3.93, 1.530),
    ("Jupiter", 71492, 1.33, 5.210),
    ("Saturn", 60268, 0.69, 9.551),
    ("Uranus", 25559, 1.27, 19.213),
    ("Neptune", 24764, 1.64, 30.070)
] # Sorted by distance from Sun

# Sort planets by size, largest first
size = lambda planet: planet[1] # second tuple field
planets.sort(key=size, reverse=True)

# Sort by density, least first
density = lambda planet: planet[2]
planets.sort(key=density)
```

## Sort Without Modifying the List

The ```sorted()``` function will return sorted data without modifying source
content. That works against tuples, as well. Hey, it works against any
iterable.

```python
# Alkaline earth metals
# sorted by atomic number
earth_metals = [
    "Beryllium",
    "Magnesium",
    "Calcium",
    "Strontium",
    "Barium",
    "Radium"
]
sorted_earth_metals = sorted(earth_metals)
sorted_earth_metals
['Barium', ..., 'Strontium']
earth_metals
['Beryllium', ..., 'Radium']
```

### Sorted Elements of a Tuple

```python
# First ten positive integers in random order
data = (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)
sorted(data)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # notice the response is a list
```

### Sorted Iterable

```python
# A string is iterable, character by character
sorted("Alphabetical")
['A', 'a', 'a', 'b', 'c', 'e', 'h', 'i', 'l', 'l', 'p', 't']
```
