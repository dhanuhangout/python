"""
Once a Counter is populated, its values can be retrieved using the dictionary
API.
"""

import collections

c = collections.Counter('abcdaab')

for letter in 'abcde':
    print('{} : {}'.format(letter, c[letter]))

# NOte: Counter doesn't raise KeyError for unknown items. If a value has not
# been seen in the input (as with e in this example), its count is 0.

'''
OUTPUT:
a : 3
b : 2
c : 1
d : 1
e : 0
'''