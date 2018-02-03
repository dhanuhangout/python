"""Because enum members are not ordered, they support only comparison
by identity and equality.
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


if __name__ == '__main__':
    actual_state = BugStatus.wont_fix
    desired_state = BugStatus.fix_released

    print('Equality:',
        actual_state == desired_state,
        actual_state == BugStatus.wont_fix)

    print('Identity:',
        actual_state is desired_state,
        actual_state is BugStatus.wont_fix)

    print('Ordered by value:')
    try:
        print('\n'.join(' ' + s.name for s in sorted(BugStatus)))
        # The greater-than and less-than comparison operators raise TypeError
        # exceptions.
    except TypeError as err:
        print(' Cannot sort: {}'.format(err))


'''
OUTPUT:
('Equality:', False, True)
('Identity:', False, True)
Ordered by value:
 Cannot sort: unorderable types: BugStatus() < BugStatus()
'''