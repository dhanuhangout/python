"""
Use most_common() to produce a sequence of the n most frequently encountered
input values and their respective counts.
"""

import collections

c = collections.Counter()

with open('/usr/share/dict/words', 'rt') as f:
    for line in f:
        c.update(line.rstrip().lower())

print('Most common:')
for letter, count in c.most_common(3):
    print('{}: {:>7}'.format(letter, count))

# Note: This example counts the letters appearing in all of the words in the
# system dictionary to produce a frequency distribution, then prints the three
# most common letters. Leaving out the argument to most_common() produces a
# list of all the items, in order of frequency.

'''
OUTPUT:
Most common:
s:   92938
e:   89420
i:   67538
'''