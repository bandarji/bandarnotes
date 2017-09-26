# Dictionaries

AKA

* Associative array
* Map

```python
post = {
    'user_id': 209,
    'message': "D5 E5 C5 C4 G4",
    'language': "English",
    'datetime': "20230215T124231Z",
    'location': (44.590533, -104.715556)
}
type(post)
# <class 'dict'>
```

```python
post2 = dict(message='SS Cotopaxi', language="English")
post2["user_id"] = 209
post2["datetime"] = "19771116T093001Z"
```

## Accessing Dictionary Entries

```python
print(post['message'])
# D5 E5 C5 C4 G4
print(post2['location'])
# KeyError exception
```

### Avoiding KeyError

#### Method One

```python
if 'location' in post2:
    print(post2['location'])
else:
    print("The post does not contain a location value.") # should say 'key'
```

#### Method Two

```python
try:
    print(post2['location'])
except KeyError:
    print("The post does not have a location.")
```

#### Method Three (Best Method)

```python
dir(post2)
help(post2.get)
loc = post2.get('location', None)
print(loc)
# None
```

## Iterate Over Dictionary

### Method One

```python
print(post)
for key in post.keys():
    value = post[key]
    print(key, '=', value)
```

### Method Two (Better Method)

SJE note: Some people will say that you should use ```iteritems()``` in place of ```items()```. That's true in older versions of Python. If you use v3, be aware that ```iteritems()``` will go away soon and that ```items()``` returns a cursor object just like the other function.

```python
for key, value in post.items():
    print(key, '=', value)
```

## Removing Data

```python
dict.pop()
dict.popitem()
dict.clear()
```
