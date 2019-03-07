"""For more complex cases, tuples might become unwidely. Since member values
can be any type of object, dictionaries can be used for cases where there are
a lot of separate attributs to track for each enum value. Complex values are
passed to __init__() as the only argument other than self.
"""

import enum


class BugStatus(enum.Enum):

    new = {
        'num': 7,
        'transitions': [
            'incomplete',
            'invalid',
            'wont_fix',
            'in_progress',
        ],
    }

    incomplete = {
        'num': 6,
        'transitions': ['new', 'wont_fix'],
    }

    invalid = {
        'num': 5,
        'transitions': ['new'],
    }

    wont_fix = {
        'num': 4,
        'transitions': ['new'],
    }

    in_progress = {
        'num': 3,
        'transitions': ['new', 'fix_committed'],
    }

    fix_committed = {
        'num': 2,
        'transitions': ['in_progress', 'fix_released'],
    }

    fix_released = {
        'num': 1,
        'transitions': ['new'],
    }

    def __init__(self, vals):
        self.num = vals['num']
        self.transitions = vals['transitions']

    def can_transition(self, new_state):
        return new_state.name in self.transitions


if __name__ == '__main__':
    print('Name: {}'.format(BugStatus.in_progress))
    print('Value: {}'.format(BugStatus.in_progress.value))
    print('Custom attribute: {}'.format(BugStatus.in_progress.transitions))
    print('Using attribute: {}'.format(
        BugStatus.in_progress.can_transition(BugStatus.new)))


'''
OUTPUT:
Name: BugStatus.in_progress
Value: {'num': 3, 'transitions': ['new', 'fix_committed']}
Custom attribute: ['new', 'fix_committed']
Using attribute: True
'''