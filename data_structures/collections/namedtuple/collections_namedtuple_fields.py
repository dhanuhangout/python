"""
Namedtuple provides several useful attributes and methods for working with
subclasses and instances. All of these built-in properties have names prefixed
with an underscore, which by convention in most python programs indicates a
private attribute. For namedtuple, however, the prefix is intended to protect
the name from collision with user-provided attribute names.

The names of the fields passed to namedtuple to define the new class are saved
in the _fields attribute.
"""

import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('Representation:', bob)
print('Fields:', bob._fields)

# Although the argument is a single space-separated string, the stored value is
# the sequence of individual names.

'''
OUTPUT:
Representation: Person(name='Bob', age=30)
Fields: ('name', 'age')
'''