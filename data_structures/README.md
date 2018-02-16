Examples in this directory are captured from this link: https://pymotw.com/3/data_structures.html

Data Structures:
Python includes several standard programming data structures, such as list, tuple, dict and set as part of its built-in types. Apart from these, standard library provides powerful and well-tested data structures. They are:

enum - Enumeration Type
collections - Container Data Types
array - Sequence of Fixed-type Data
heapq - Heap Sort Algorithm
bisect - Maintain Lists in Sorted Order
queue - Thread-Safe FIFO Implementation
struct - Binary Data Structures
weakref - Impermanent References to Objects
copy - Duplicate Objects
pprint - Pretty-Print Data Structures


enum - this module provides and implementation of an enumeration type, with iteration and comparison capabilities.
It can be used to create well-defined symbols for values, instead of using literal strings or integers.

collections - This module includes implementation of serveral data structures that extend those found in other modules. The data types are ChainMap, Counter, defaultdict, deque, namedtuple, OrderedDict and collections.abc

array -  For large amounts of data, an array may make more efficient use of memory than a list. Since the array is limited to a single data type, it can use a more compact memory representation than a general-purpose list.

heapq - The functions in heapq modify the contents of a list while preserving the sort order of the list with low overhead.

bisect - It uses a binary search to find the insertion point for new items, and is an alternative to repeatedly sorting a list that changes freqently.

queue - Although the built-in list can simulate a queue using the insert() and pop() methods, it is not thread-safe. For true ordered communication between threads use the queue module. multiprocessing includes a version of a Queue that works between processes, making it easier to convert a multithreaded program to use processes instead.

struct - It is useful for decoding data from another application, perhaps coming from a binary file or stream of data, into Python’s native types for easier manipulation.

weakref - For highly interconnected data structures, such as graphs and trees, use weakref to maintain references while still allowing the garbage collector to clean up objects after they are no longer needed.

copy - The functions in this module are used for duplicating data structures and their contents, including making recursive copies with deepcopy().

pprint - It is used to create easy-to-read representations that can be printed to the console or written to a log file for easier debugging.