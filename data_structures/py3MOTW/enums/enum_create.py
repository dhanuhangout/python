"""Notes on enumeration type.

The enum module defines an enumeration type with iteration and comparison
capabilities. It can be used to create well-defined symbols for values, instead
of using literal integers or strings.
"""

import enum


class BugStatus(enum.Enum):
    """A new enumeration is defined using the class syntax by subclassing Enum
    and adding class attributes describing the values."""

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


if __name__ == '__main__':
    print('\nMember name: {}'.format(BugStatus.wont_fix.name))
    print('\nMember value: {}'.format(BugStatus.wont_fix.value))

'''
OUTPUT:

Member name: wont_fix

Member value: 4
'''