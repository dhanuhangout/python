"""To require all members to have unique values, add the @unique decorator
to the Enum.
"""

import enum


@enum.unique
class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

    # This will trigger an error with unique applied.
    by_design = 4
    closed = 1
    # Members with repeated values trigger a ValueError exception when the
    # Enum class is being interrupted.


'''
OUTPUT:
$ python3 enum_unique_enforce.py 
Traceback (most recent call last):
  File "enum_unique_enforce.py", line 9, in <module>
    class BugStatus(enum.Enum):
  File "/usr/lib/python3.5/enum.py", line 573, in unique
    (enumeration, alias_details))
ValueError: duplicate values found in <enum 'BugStatus'>: by_design -> wont_fix, closed -> fix_released
'''