# Logging

* Six default logging levels

| Logging Level | Numeric Value |
| --- | --- |
| NOTSET | 0 |
| DEBUG | 10 |
| INFO | 20 |
| WARNING | 30 (Default ) |
| ERROR | 40 |
| CRITICAL | 50 |

* Loggers will only write messages with the level greater than or equal to set level

## Fail to Write Due to Logging Level

```python
import logging

# Create and configure logger
logging.basicConfig(filename='/tmp/Lumberjack.Log')
logger = logging.getLogger()

logger.info("Our first message.") # Nothing written to log though

print(logger.level) # 30
```

## Corrected / Now Writes With Timestamp

```python
import logging

# Create and configure logger
LOG_FORMAT = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename='/tmp/Lumberjack.Log', level=logging.DEBUG,
                    format=LOG_FORMAT, filemode = 'w')
logger = logging.getLogger()

logger.info("Our SECOND message.")

print(logger.level) # 10
```

## Log Levels

```python
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!") # [sic]
```

## Example

```python
import logging
import math

# Create and configure logger
LOG_FORMAT = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename='/tmp/Lumberjack.Log', level=logging.DEBUG,
                    format=LOG_FORMAT, filemode = 'w')
logger = logging.getLogger()

def quadratic_formula(a, b, c):
    """Return the solutions to the equation ax^2 + bx + c = 0."""
    logger.info("quadratic_formula({0}, {1}, {2}".format(a, b, c))
    # Compute the discriminant
    logger.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c
    # Compute the two roots
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)
    # Return the roots
    logger.debug("# Return the roots")
    return (root1, root2)

roots = quadratic_formula(1, 0, -4)
print(roots) # (2.0, -2.0)
```
