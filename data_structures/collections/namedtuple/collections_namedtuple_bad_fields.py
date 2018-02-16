"""
Field names are invalid if they are repeated or conflict with Python keywords.
"""

import collections

try:
	collections.namedtuple('Person', 'name class age')
except ValueError as err:
	print(err)

try:
	collections.namedtuple('Person', 'name class age')
except ValueError as err:
	print(err)

# As the field names are parsed, invalid values cause ValueError exceptions.

'''
OUTPUT:
Type names and field names cannot be a keyword: 'class'
Type names and field names cannot be a keyword: 'class'
'''