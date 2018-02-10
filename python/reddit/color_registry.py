#!/usr/bin/env python

def add_to_registry():
    finished = False
    name = None
    color = None
    input_ = input('Name and color: ')
    try:
        name, color = input_.split()
    except ValueError:
        finished = True # No input or bad input provided, time to quit
    return finished, name, color

def main():
    finished = False
    registry = {}
    while not finished:
        finished, name, color = add_to_registry()
        if name and color:
            if name not in registry:
                registry[name] = color
            else:
                print(f'{name} already in registry.')
        else:
            finished = True
    for name, color in registry.items():
        print(f'{name} {color}')

if __name__ == '__main__':
    main()