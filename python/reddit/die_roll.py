# Guess Die Roll

```python
roll_again = True
while roll_again:
    die_roll = str(random.randint(1, 6))
    guess = input('What is your die roll guess? ')
    if guess == die_roll:
        print('You guessed correctly!')
    else:
        print('You guessed {}, but rolled {}.'.format(guess, die_roll))
    try_again = input('Try again? [Y/N] ')
    if try_again.lower() in ['no', 'n']:
        roll_again = False
```
