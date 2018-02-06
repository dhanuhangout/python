"""
The _replace() method builds a new instance, replacing the values of some
fields in the process.
"""

import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('Before:', bob)
bob2 = bob._replace(name='Robert')
print('After:', bob2)
print('Same?:', bob is bob2)

'''
OUTPUT:
Before: Person(name='Bob', age=30)
After: Person(name='Robert', age=30)
Same?: False
'''