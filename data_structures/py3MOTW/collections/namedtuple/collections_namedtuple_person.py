"""
Namedtuple instances are just as memory efficient as regular tuples because
they do not have per-instance dictionaries.
Each kind of namedtuple is represented by its own class, which is created by
using the namedtuple() factory function.
The arguments are the name of the new class and a string containing the names
of the elements.
"""

import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('Representation: ', bob)

jane = Person(name='Jane', age=29)
print('Field by name: ', jane.name)

print('Fields by index:')
for p in [bob, jane]:
	print('{} is {} years old'.format(*p))

'''
Notes:
It is possible to access the fields of the namedtuple by name using dotted
notation (obj.attr) as well as by using positional indexes of standard tuples.
Just like a regular tuple, a namedtuple is immutable. This restriction allows
tuple insances to have a consistent hash value, which makes it possible to use
them as keys in dictionaris and to be included in sets.
'''

'''
OUTPUT:
Representation:  Person(name='Bob', age=30)
Field by name:  Jane
Fields by index:
Bob is 30 years old
Jane is 29 years old
'''