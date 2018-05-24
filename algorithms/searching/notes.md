Ref: Problem Solving with Algorithm and Data Structures.  
http://interactivepython.org/runestone/static/pythonds/SortSearch/searching.html

# Table of Contents
1. [Introduction](#section1)
2. [Types of searching techniques](#section2)
    2.1. [Sequential Search](#section2.1)
    2.2. [Binary Search](#section2.2)
3. [How to run code](#section3)

## Introduction <a name="section1"></a>
Searching is the algorithmic process of finding a particular item in a  
collection of items.  
A search typically answers either True or False as to whether the time is  
present. On occasion it may be modified to return where the item is found.  

In python, there is a very easy way to ask whether an item is in a list of  items using "in" operator.  
Eg:  
>>> 15 in [3, 5, 2, 4, 1]  
False  
>>> 3 in [3, 5, 2, 4, 1]  
True  

## Types of searching techniques <a name="section2"></a>  
1. Linear or Sequential search  
2. Binary search  


### 1. Sequential Search <a name="section2.1"></a>  
When items are stored in a collection such as a list, we say that they have a  
linear or sequential relationship.  
Starting at the first item in the list, we simply move from item to next item,  
following the underlying sequential ordering until we either find what we are  
looking for or run out of items. If we run out of items, we have discovered  that the item we were searching for was not present.  
There are two scenarios involved:  
1. Un-ordered list of items. ([1, 2, 32, 8, 17, 19, 42, 13, 0])  
2. Ordered list of items. ([0, 1, 2, 8, 13, 17, 19, 32, 42,])  

Analysis:  
- If the item is not in the list, the only way to know it is to compare it   against every item present. So, if there are n items, then the sequential   search requires n comparisons to discover that the item is not there.  
- If the item is in list, there are three different scenarios that can occur.  
  * In best case, we will find the item at the beginning of the list. We will  need only one comparison.  
  * In worst case, we will not discover the item until the very last  comparison, the nth comparison.  
  * In average case, we will find the item about halfway into the list; that   is, we will compare against n/2 items.  
Based on this analysis, teh complexity of sequential search is O(n).  


### 2. Binary Search <a name="section2.2"></a>  
Binary search will start by examining the middle item. If that item is the one we are searching for, we are done. If it is not the correct item, we can use the ordered nature of the list to eliminate half of the remaining items.
In an ordered list, if the item we are searching is greater than the middle item, we know that the entire lower half of the list as well as the middle item can be eliminated from further consideration. The item, if it is in the list, must be in the upper half.
We can then repeat the process with the upper half. S 

## How to run code <a name="section3"></a>  
$ bazel run :searching_algs_bin  
$ bazel test :searching_algs_test --test_output=all  
