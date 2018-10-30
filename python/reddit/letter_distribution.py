import random
import string

distribution = {}
for _ in range(100000):
    character = random.choice(string.lowercase)
    distribution[character] = distribution.get(character, 0) + 1
for character in string.lowercase:
    print('{}: {}'.format(character, distribution.get(character, 0)))
most_frequent = max(distribution.items(), key=lambda r: r[1])
least_frequent = min(distribution.items(), key=lambda r: r[1])
print('\n')
print('most frequent: {} ({})'.format(most_frequent[0], most_frequent[1]))
print('least frequent: {} ({})'.format(least_frequent[0], least_frequent[1]))
