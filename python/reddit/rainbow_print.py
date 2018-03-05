import random
import sys

def rainbow(message):
    if isinstance(message, str):
        colors = [
            '\033[31;1m', # red
            '\033[32;1m', # green
            '\033[33;1m', # yellow
            '\033[34;1m', # blue
            '\033[35;1m', # magenta
            '\033[36;1m', # cyan
        ]
        reset = '\033[0m'
        message_length = len(message)
        for letter in message:
            out = '{}{}'.format(random.choice(colors), letter)
            sys.stdout.write(out)
            sys.stdout.flush()
        sys.stdout.write('{}{}'.format(reset, '\n'))
        sys.stdout.flush()


rainbow('Hello, World!')
