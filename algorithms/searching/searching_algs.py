'''Searching techniques.'''

class SearchingAlgs(object):
    '''Class that performs searching techniques on given data.'''

    def unorderedSequentialSearch(self, alist, item):
        '''Search an item using sequential/linear search technique .'''
        pos = 0
        found = False

        while pos < len(alist) and not found:
            if alist[pos] == item:
                found = True
            else:
                pos = pos+1

        return found

    def orderedSequentialSearch(self, alist, item):
        '''Search an item in an ordered list using sequential search technique.'''
        pos = 0
        found = False
        stop = False

        while pos < len(alist) and not found and not stop:
            if alist[pos] == item:
                found = True
            else:
                if alist[pos] > item:
                    stop = True
                else:
                    pos = pos+1

        return found



if __name__ == '__main__':
    unordered_testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    SEARCHING_ALG_OBJ = SearchingAlgs()
    # Negative test case.
    print(SEARCHING_ALG_OBJ.unorderedSequentialSearch(unordered_testlist, 3))
    # Positive test case.
    print(SEARCHING_ALG_OBJ.unorderedSequentialSearch(unordered_testlist, 13))

    ordered_testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    # Negative test case.
    print(SEARCHING_ALG_OBJ.orderedSequentialSearch(ordered_testlist, 3))
    # Positive test case.
    print(SEARCHING_ALG_OBJ.orderedSequentialSearch(ordered_testlist, 13))