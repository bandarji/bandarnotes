# Text Files

Learn to read and write text files.

## Open a File

```python
f = open("guido_bio.txt")
text = f.read()
f.close()
print(text)
```

This method is simple, but does not deal with problems well, like something
going wrong before the file close.

```python
with open("guido_bio.txt") as fobj:
    bio = fobj.read()
```

This works better because the file will close, even if exceptions occur.

## File Not Found

```python
try:
    with open("future_lottery_numbers.txt") as f:
        text = f.read()
except FileNotFoundError:
    text = None
print(text)
```

## Write a File

```python
oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]
with open("oceans.txt", "w") as f:
    for ocean in oceans:
        f.write(ocean)
```

Using 'w' will create a new file if one does not exist. It will overwrite an
existing file. So, be careful. The above code will not place the ocean names on
separate lines. Fixing that...

```python
oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]
with open("oceans.txt", "w") as f:
    for ocean in oceans:
        f.write(ocean)
        f.write("\n")
```

Or:

```python
oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]
with open("oceans.txt", "w") as f:
    for ocean in oceans:
        print(ocean, file=f)
```

### Appending File Writes

Append mode ("a") will create a file if not found. Instead of overwriting an
existing file, it will add content to the file's end.

```python
with open("oceans.txt", "a") as f:
    print(23*"=", file=f)
    print("These are the 5 oceans.", file=f)
```
