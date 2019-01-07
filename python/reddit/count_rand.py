#!/usr/bin/env python

import random

def count_the_rands(target=1, floor=1, ceiling=1000):
    count = 0 # how many random numbers generated
    numbers = {} # keeping track of the numbers generated
    number = None # the number we generate each cycle
    while number != target:
        number = random.randint(floor, ceiling)
        count += 1 # increment counter
        numbers[number] = numbers.get(number, 0) + 1 # add to number dictionary
    print('To find the target {}, we looped {} times.'.format(target, count))
    most_common = sorted(numbers.items(), key=lambda r: r[1], reverse=True)[0][0]
    least_common = sorted(numbers.items(), key=lambda r: r[1])[0][0]
    print('Most common number: {}'.format(most_common))
    print('Lest common number: {}'.format(least_common))
    print('')

def main():
    random.seed(1)
    tests = [
        {'target': 15, 'floor': 1, 'ceiling': 100},
        {'target': 20, 'floor': 1, 'ceiling': 1000},
        {'target': 25, 'floor': 1, 'ceiling': 10000},
        {'target': 50, 'floor': 1, 'ceiling': 100000},
    ]
    for test in tests:
        count_the_rands(**test)

if __name__ == '__main__':
    main()
