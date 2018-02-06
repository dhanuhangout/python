"""
Trying to change a value through its named attribute results in an
AttributeError.
"""

import collections

Person = collections.namedtuple('Person', 'name age')

pat = Person(name='Pat', age=12)
print('Representation:', pat)

pat.age = 21


'''
OUTPUT:
Representation: Person(name='Pat', age=12)
Traceback (most recent call last):
  File "collections_namedtuple_immutable.py", line 13, in <module>
    pat.age = 21
AttributeError: can't set attribute
'''