"""For more control over the values associated with members, the names string
can be replaced with a sequence of two-part tuples or a dictionary mapping
names to values.
"""

import enum


BugStatus = enum.Enum(
    value = 'BugStatus',
    names = [
        ('new', 7),
        ('incomplete', 6),
        ('invalid', 5),
        ('wont_fix', 4),
        ('in_progress', 3),
        ('fix_committed', 2),
        ('fix_released', 1),
    ],
)


if __name__ == '__main__':
    print('All members:')
    for status in BugStatus:
        print('{:15} = {}'.format(status.name, status.value))
    # Notes: In this example, a list of two-part tuples is given instead of a
    # single string containing only the member names. This makes it possible to
    # resconstruct the BugStatus enum with the members in the same order as the
    # version defined in enum_create.py


'''
OUTPUT:
All members:
new             = 7
incomplete      = 6
invalid         = 5
wont_fix        = 4
in_progress     = 3
fix_committed   = 2
fix_released    = 1
'''