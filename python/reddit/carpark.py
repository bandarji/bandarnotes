#!/usr/bin/env python

"""Carpark Simulation

On 15-minute intervals, for a random number of cars arriving to a garage (1-20),
with some random number departing (1-${arrived}), display time, cars added,
cars departed and cars remaining. Exit the program after the lot has more than
one hundred cars remaining. Requires a function for arriving count and another
for departing count.
"""

import random

cars_arrive = lambda: random.randint(1, 20)
cars_depart = lambda arrived: random.randint(1, arrived)

def display_header():
  print('{:^64}\n'.format('Carpark Simulation'))
  print('{:<15} {:>15} {:>15} {:>15}'.
        format('Time', 'Added', 'Removed', 'Remaining'))
  print('='*63)

def display_status(timestamp, arrived, departed, remaining):
  hours = str(timestamp // 60).zfill(2)
  minutes = str(timestamp % 60).zfill(2)
  display_time = '{}:{}'.format(hours, minutes)
  print('{:<15} {:>15} {:>15} {:>15}'.
        format(display_time, arrived, departed, remaining))

def main():
  # random.seed(1) ### for predictable/consistent output
  display_header()
  remaining = 0
  timestamp = 0
  while remaining <= 100:
    arrived = cars_arrive()
    departed = cars_depart(arrived)
    remaining += arrived - departed
    display_status(timestamp, arrived, departed, remaining)
    timestamp += 15

if __name__ == '__main__':
  main()
