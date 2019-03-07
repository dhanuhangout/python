"""
Note: ChainMap is availble in Python3. But not in Python2.7.
The ChainMap class manages a sequence of dictionaries, and searches through
them in the order they are given to find values associated with keys. A
ChainMap makes a good "context" container, since it can be treated as a stack
for which manages happen as the stack grows, with these changes being discarded
again as the stack shrinks.
"""

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

print('Individual Values')
print('a = {}'.format(m['a']))
print('b = {}'.format(m['b']))
print('c = {}'.format(m['c']))
print()

# Notes: The ChainMap supports the same API as a regular dictionary for
# accessing existing values. (apis - items, keys, values)

print('Keys = {}'.format(list(m.keys())))
print('Values = {}'.format(list(m.values())))
print()

print('Items:')
for k, v in m.items():
    print('{} = {}'.format(k, v))
print()

print('"d" in m: {}'.format(('d' in m)))


'''
OUTPUT:
$ python3 collections_chainmap_read.py 
Individual Values
a = A
b = B
c = C

Keys = ['b', 'c', 'a']
Values = ['B', 'C', 'A']

Items:
b = B
c = C
a = A

"d" in m: False
'''