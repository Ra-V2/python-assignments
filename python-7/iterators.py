import itertools
import random

# Iterators

# A
print('A\n')
counter = itertools.cycle([0, 1])
for _ in range(10):
    print(next(counter))

# B
print('\nB\n')
directions = ['N', 'E', 'S', 'W']
random.shuffle(directions)
direction_cycle = itertools.cycle(directions)
for _ in range(10):
    print(next(direction_cycle))

# C
print('\nC\n')
weekdays = itertools.cycle([0, 1, 2, 3, 4, 5, 6])
for _ in range(10):
    print(next(weekdays))