"""Enum member values are not restricted to integers. In fact, any type of
object can be associated with a member. If the value is a tuple, the members
are passed as individual arguments to __init__().
"""

import enum


class BugStatus(enum.Enum):
    """Non-integer Member Values."""

    new = (7, ['incomplete',
               'invalid',
               'wont_fix',
               'in_progress'])
    incomplete = (6, ['new', 'wont_fix'])
    invalid = (5, ['new'])
    wont_fix = (4, ['new'])
    in_progress = (3, ['new', 'fix_committed'])
    fix_committed = (2, ['in_progress', 'fix_released'])
    fix_released = (1, ['new'])

    def __init__(self, num, transitions):
        self.num = num
        self.transitions = transitions

    def can_transition(self, new_state):
        return new_state.name in self.transitions


if __name__ == '__main__':
    print('Name: {}'.format(BugStatus.in_progress))
    print('Value: {}'.format(BugStatus.in_progress.value))
    print('Custom attribute: {}'.format(BugStatus.in_progress.transitions))
    print('Using attribute: {}'.format(
        BugStatus.in_progress.can_transition(BugStatus.new)))
    # Notes: In this example, each member value is a tuple containing the
    # numerical ID (such as might be stored in a database) and a list of valid
    # transitions away from the current state.


'''
OUTPUT:
Name: BugStatus.in_progress
Value: (3, ['new', 'fix_committed'])
Custom attribute: ['new', 'fix_committed']
Using attribute: True
'''