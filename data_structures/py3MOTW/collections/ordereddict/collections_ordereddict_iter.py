"""
An OrderedDict is a dictionary subclass that rememebers the order in which its
contents are added.
"""

import collections

print('Regular dictionary:')
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'

for k, v in d.items():
	print(k, v)

print('OrderedDict:')
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'

for k, v in d.items():
	print(k, v)

'''
Notes:
A regular dict does not track the insertion order, and iterating over it
produces the values based on how the keys are stored in the hash table, which
is in turn influenced by a random value to reduce collisions.
In an OrderdDict, by contrast, the order in which the items are inserted is
remembered and used when creating an iterator.
'''

'''
OUTPUT:
Regular dictionary:
a A
b B
c C
OrderedDict:
a A
b B
c C
'''