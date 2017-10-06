'''Sorting linked list.'''

#pylint: disable=too-few-public-methods
class Node(object):
    '''Class contains data and link.'''
    def __init__(self):
        self.data = None
        self.link = None


class SortList01(object):
    '''Sorting linked list.'''
    def __init__(self):
        self.node = Node()
        self.start = Node()
        self.visit = Node()
        self.newnode = Node()

    def read_userdata(self):
        '''Reads user input and appends it to the list.'''
        user_choice = 'y'
        while user_choice == 'y' or user_choice == 'Y':
            val = raw_input('Enter an integer value: ')
            add_atend(num)
            user_choice = raw_input('Do you want to enter new value (Y/N) or (y/n): ')

    def add_atend(self, num):
        '''Appends node at the end of list.'''
        if self.node.data is None:
            self.node.data = num
        else:
            temp = self.node
            # Traverse till the end of list.
            while temp.link is not None:
                temp = temp.link
            # Create a new node and add it to the end of list.
            new_node = Node()
            new_node.data = num
            temp.link = new_node

    def display_list(self):
        '''Display all elements present in the list.'''
        temp = self.node
        print 'Contents of linked list are:'
        while temp.link is not None:
            print temp.data
            temp = temp.link
        if temp.data is not None and temp.link is None:
            print temp.data

    def count(self):
        '''Counts number of elements present in the list.'''
        temp = self.node
        count = 0
        while temp.link is not None:
            count += 1
            temp = temp.link
        if temp.data is not None and temp.link is None:
            count += 1
        return count

    def selection_sort_nocount_use(self):
        '''Perform selection sort technique on given linked list.'''
        # Selection sort does positional comparision. i.e., compare element at
        # 1st position with all elements till end of list and swap if required.
        # Then move on to 2nd position and perform the same. And so on...
        p = self.node
        traverse_node = self.node
        coun = 0
        if self.node.data is None:
            print 'No elements present in given list.'
        else:
            while p.link is not None:
                q = p.link
                while q.link is not None:
                    # Arrange list in ascending order.
                    #print 'before if: p.data = ', p.data, 'q.data = ', q.data
                    if p.data > q.data:
                        temp = p.data
                        p.data = q.data
                        q.data = temp
                        # print 'inside if: p.data = ', p.data, 'q.data = ', q.data
                    q = q.link
                    coun += 1
                    print 'After %d iteration:' % coun
                    self.display_list()
                    #print 'after if: p.data = ', p.data, 'q.data = ', q.data
                if q.data is not None and q.link is None:
                    if p.data < q.data:
                        temp = p.data
                        p.data = q.data
                        q.data = temp
                p = p.link
            # print 'last element = ', p.data, 'q = ', q.data
            # print 'self.node.data = ', self.node.data

            # Perform bubble sort on last element.
            if p.data is not None and p.link is None:
                while traverse_node.link is not None:
                    if p.data < traverse_node.data:
                        temp = p.data
                        p.data = traverse_node.data
                        traverse_node.data = temp
                    traverse_node = traverse_node.link
                if traverse_node.data is not None and traverse_node.link is None:
                    if p.data < traverse_node.data:
                        temp = p.data
                        p.data = traverse_node.data
                        traverse_node.data = temp
                    traverse_node = traverse_node.link

    def bubble_sort(self):
        '''Perform bubble sort technique on given linked list.'''
        # Bubble sort works by comparing each element in the list with the
        # element next to it and swapping them if required.
        p = self.node
        traverse_node = self.node
        '''coun = 0
        is_swapped = 1
        if self.node.data is None:
            print 'No elements present in given list.'
        else:
            while is_swapped > 0:
                p = self.node
                q = p.link
                while p.link is not None:
                    if p.data > q.data:
                        # Do swap
                        temp = p.data
                        p.data = q.data
                        q.data = temp
                        is_swapped = True'''


if __name__ == '__main__':
    BUBBLE_SORT_LIST = SortList01()
    BUBBLE_SORT_LIST.add_atend(9)
    BUBBLE_SORT_LIST.add_atend(8)
    BUBBLE_SORT_LIST.add_atend(7)
    BUBBLE_SORT_LIST.add_atend(6)
    BUBBLE_SORT_LIST.add_atend(5)
    BUBBLE_SORT_LIST.add_atend(4)
    BUBBLE_SORT_LIST.add_atend(3)
    BUBBLE_SORT_LIST.add_atend(2)
    BUBBLE_SORT_LIST.add_atend(1)

    #BUBBLE_SORT_LIST.display_list()

    #print 'Number of elements in linked list is: ', BUBBLE_SORT_LIST.count()

    BUBBLE_SORT_LIST.bubble_sort()

    print 'Elements after bubble sort:'
    BUBBLE_SORT_LIST.display_list()

    SELECT_SORT_LIST = SortList01()
    SELECT_SORT_LIST.add_atend(9)
    SELECT_SORT_LIST.add_atend(8)
    SELECT_SORT_LIST.add_atend(7)
    SELECT_SORT_LIST.add_atend(6)
    SELECT_SORT_LIST.add_atend(5)
    SELECT_SORT_LIST.add_atend(4)
    SELECT_SORT_LIST.add_atend(3)
    SELECT_SORT_LIST.add_atend(2)
    SELECT_SORT_LIST.add_atend(1)


    #SELECT_SORT_LIST.display_list()

    #print 'Number of elements in linked list is: ', SELECT_SORT_LIST.count()

    #SELECT_SORT_LIST.selection_sort()

    #print 'Elements after selection sort:'
    #SELECT_SORT_LIST.display_list()
