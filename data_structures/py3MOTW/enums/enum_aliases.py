"""Enum members with the same value are tracked as alias references to the same
member object. Aliases do not cause repeated values to be present in the
iterator for the Enum.
"""

import enum


class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

    by_design = 4
    closed = 1


if __name__ == '__main__':
    for status in BugStatus:
        print('{:15} = {}'.format(status.name, status.value))

    print('Same: by_design is wont_fix: {}'.format( 
        BugStatus.by_design is BugStatus.wont_fix))
    print('Same: closed is fix_released: {}'.format(
        BugStatus.closed is BugStatus.fix_released))
    # Because by_design and closed are aliases for other members, they do not
    # appear separately in the output when iterating over the Enum. The
    # canonical name of a member is the first name attached to the value.


'''
OUTPUT:
fix_released    = 1
fix_committed   = 2
in_progress     = 3
wont_fix        = 4
invalid         = 5
incomplete      = 6
new             = 7
Same: by_design is wont_fix: True
Same: closed is fix_released: True
'''