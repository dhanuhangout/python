"""
A Counter is a container that keeps track of how many times equivalent values
are added. It can be used to implement the same algorithms for which other
languages commonly use bag or multiset data structures.

Counter supports three forms of initialization. Its constructor can be called
with a sequence of items, a dictionary containing keys and counts, or using
keyword arguments that map string names to counts.
"""

import collections

print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print(collections.Counter({'a': 2, 'b': 3, 'c': 1}))
print(collections.Counter(a=2, b=3, c=1))

'''
OUTPUT:
Counter({'b': 3, 'a': 2, 'c': 1})
Counter({'b': 3, 'a': 2, 'c': 1})
Counter({'b': 3, 'a': 2, 'c': 1})
'''