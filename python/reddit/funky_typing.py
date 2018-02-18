# Funky Typing

```python
import random
import sys
import time

def funky_typing(message):
    for c in message:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2 * random.random())

funky_typing('All work and no play make Homer something, something.')
```
