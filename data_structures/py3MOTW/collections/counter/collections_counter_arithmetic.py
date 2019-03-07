"""
Counter instances support arithmetic and set operations for aggregating
results. This example shows the standard operators for creating new Counter
instances, but the in-place operators +=, -=, &= and |= are also supported.
"""

import collections

c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print('C1: ', c1)
print('C2: ', c2)

print('\nCombined counts:')
print(c1 + c2)

print('\nSubtraction:')
print(c1 - c2)

print('\nIntersection (taking positive minimums):')
print(c1 & c2)

print('\nUniion (taking maximums):')
print(c1 | c2)

# Note: Each time a new Counter is produced through an operation, any items
# with zero or negative counts are discarded. The count for a is the same in c1
# and c2, so subtraction leaves it at zero.

'''
OUTPUT:
('C1: ', Counter({'b': 3, 'a': 2, 'c': 1}))
('C2: ', Counter({'a': 2, 'b': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 1, 't': 1}))

Combined counts:
Counter({'a': 4, 'b': 4, 'c': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 1, 't': 1})

Subtraction:
Counter({'b': 2, 'c': 1})

Intersection (taking positive minimums):
Counter({'a': 2, 'b': 1})

Uniion (taking maximums):
Counter({'b': 3, 'a': 2, 'c': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 1, 't': 1})
'''