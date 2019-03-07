# 1. PYTHON PRIMER


## 1.1 Python Overview:
### 1.1.1 Python Interpreter:
Python is formally an integrated language.
Using "-i" flag we can execute a script and then enter interactive mode (e.g., python -i demo.py)

### 1.1.2 Preview of a Python Program
Python's syntax relies heavily on the use of whitespace.
Individual statements are typically concluded with a newline character, although a command can extend to another line, either with a concluding backslash character (\).

## 1.2 Objects in Python
Python is an object-oriented language and classes form the basis for all data types.

### 1.2.1 Identifiers, Objects, and the Assignment Statement
Identifiers (Reseved Words):
False       as      continue     else    from    in       not     return  yield
None        assert  def          except  global  is       or      try
Ture        break   del          finally if      lambda   pass    while
and         classes elif         for     import  nonlocal raise   with

### 1.2.2 Creating and Using Objects

### 1.2.3 Built-In Classes
A class is immutable if each object of that class has a fixed value upon instantiation that cannot subsequently be changed.

<table>
  <tr>
    <th>Class</th>
    <th>Description</th>
    <th>Immutable?</th>
  </tr>

  <tr>
    <td>bool</td>
    <td>Boolean value</td>
    <td>&#x2611;</td>
  </tr>

  <tr>
    <td>int</td>
    <td>integer</td>
    <td>&#9745;</td>
  </tr>

  <tr>
    <td>float</td>
    <td>floating point number</td>
    <td>&#9745;</td>
  </tr>

  <tr>
    <td>list</td>
    <td>mutable sequence of objects</td>
    <td>&#9745;</td>
  </tr>

  <tr>
    <td>tuple</td>
    <td>immutable sequence of objects</td>
    <td>&#9745;</td>
  </tr>

  <tr>
    <td>str</td>
    <td>character string</td>
    <td>&#9745;</td>
  </tr>

  <tr>
    <td>set</td>
    <td>unordered set of distinct objects</td>
    <td>&#x2612;</td>
  </tr>

  <tr>
    <td>frozen set</td>
    <td>immutable form of set class</td>
    <td>&#9745;</td>
  </tr>

  <tr>
    <td>dict</td>
    <td>associative mapping</td>
    <td>&#9746;</td>
  </tr>
</table>

set and frozenset classes:
set class represents the mathemtical notion of a set, namely a collection of elements, without duplicates and without an inherent order to those elsements.
Advantage - As opposed to a list, is that it has a hightly optimized method for checking whether a specific element is contained in the set. This is based on a data structure known as a hash table.
eg: set - {'red', 'green', 'blue'}
Restrictions -
(1) The set doesn't maintain the elements in any particular order.
(2) Only instances, floating-point numbers, and character strings are eligble to be elements of a set.
It is possible to maintain a set of tuples, but not a set of lists or a set of sets, as lists and sets are mutable.

frozen set class is an immutable form of the set type, so it is legal to have a set of frozensets.


## 1.3 Expressions, Operators, and Precedence

Logical Operators

<table>
  <tr>
    <tr><th>Logical Operators</th>
    <td>not</td>
    <td>and</td>
    <td>or</td>
  </tr>
    <th>Equlity Operators</th>
    <td>is</td>
    <td>is not</td>
    <td>==</td>
    <td>!=</td>
  </tr>
</table>