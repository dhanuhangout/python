Ref: Problem Solving with Algorithm and Data Structures.
http://interactivepython.org/runestone/static/pythonds/SortSearch/searching.html

Searching is the algorithmic process of finding a particular item in a
collection of items.
A search typically answers either True or False as to whether the time is
present. On occasion it may be modified to return where the item is found.

In python, there is a very easy way to ask whether an item is in a list of items
using "in" operator.
Eg:
>>> 15 in [3, 5, 2, 4, 1]
False
>>> 3 in [3, 5, 2, 4, 1]
True

Types of searching techniques:
Linear or Sequential search
Binary search


Sequential Search:
When items are stored in a collection such as a list, we say that they have a
linear or sequential relationship.
Starting at the first item in the list, we simply move from item to next item,
following the underlying sequential ordering until we either find what we are
looking for or run out of items. If we run out of items, we have discovered that the item we were searching for was not present.
There are two scenarios involved:
1. Un-ordered list of items. ([1, 2, 32, 8, 17, 19, 42, 13, 0])
2. Ordered list of items. ([0, 1, 2, 8, 13, 17, 19, 32, 42,])

Analysis:
- If the item is not in the list, the only way to know it is to compare it against every item present. So, if there are n items, then the sequential search requires n comparisons to discover that the item is not there.
- If the item is in list, there are three different scenarios that can occur.
  * In best case, we will find the item at the beginning of the list. We will need only one comparison.
  * In worst case, we will not discover the item until the very last comparison, the nth comparison.
  * In average case, we will find the item about halfway into the list; that is, we will compare against n/2 items.
Based on this analysis, teh complexity of sequential search is O(n).


How to run code:
$ bazel run :searching_algs_bin
$ bazel test :searching_algs_test --test_output=all
