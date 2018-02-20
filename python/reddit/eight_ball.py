# Magic Eight Ball

## Using Dictionary Instead of Long `if`, `elif`, `else` Sequence

```python
def eight_ball(number):
    choices = {
        '1': 'It is certain',
        '2': 'It is decidedly so',
        '3': 'Yes',
        '4': 'Reply hazy, try again',
        '5': 'Ask again later',
        '6': 'Concentrate and ask again',
        '7': 'My reply is no',
    }
    return choices.get(str(number), 'Very doubtful')

print(eight_ball(1))
print(eight_ball(999))
print(eight_ball('he loves me?'))
```

## Using `lambda` function

```python
eight_ball = lambda c: {
        '1': 'It is certain',
        '2': 'It is decidedly so',
        '3': 'Yes',
        '4': 'Reply hazy, try again',
        '5': 'Ask again later',
        '6': 'Concentrate and ask again',
        '7': 'My reply is no',
    }.get(c, 'Very doubtful')

print(eight_ball(str(1)))
```
