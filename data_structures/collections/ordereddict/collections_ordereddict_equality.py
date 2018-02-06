"""
A regular dict looks at its contents when testing for equality. An OrderedDict
also considers the order in which the items are added.
"""

import collections

print('Regular dictionary:')
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = {}
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)

print('OrderedDict:', end=' ')

d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = collections.OrderedDict()
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)

# In this case, since the two ordered dictionaries are created from values in
# a different order, they are considered to be different.

'''
OUTPUT:
Regular dictionary:
True
OrderedDict: False
'''