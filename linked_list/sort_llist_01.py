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

    def selection_sort(self):
        '''Perform selection sort technique on given linked list.'''
        print 'selection sort'

    def bubble_sort(self):
        '''Perform bubble sort technique on given linked list.'''
        # Bubble sort works by comparing each element of the list with the
        # element next to it and swapping them if required.
        p = self.node
        # q = Node()
        # q = p.link
        traverse_node = self.node
        if self.node.data is None:
            print 'No elements present in given list.'
        else:
            while p.link is not None:
                q = p.link
                while q.link is not None:
                    # Arrange list in ascending order.
                    print 'before if: p.data = ', p.data, 'q.data = ', q.data
                    if p.data > q.data:
                        temp = p.data
                        p.data = q.data
                        q.data = temp
                        print 'inside if: p.data = ', p.data, 'q.data = ', q.data
                    q = q.link
                    print 'after if: p.data = ', p.data, 'q.data = ', q.data
                if q.data is not None and q.link is None:
                    if p.data < q.data:
                        temp = p.data
                        p.data = q.data
                        q.data = temp
                p = p.link
            '''print 'last element = ', p.data, 'q = ', q.data, 'traverse_node.data = ', traverse_node.data, 'self.node.data = ', self.node.data, self.node.link.data
            if p.data is not None and p.link is None:
                while traverse_node.link is not None:
                    if p.data > traverse_node.data:
                        temp = p.data
                        p.data = traverse_node.data
                        traverse_node.data = temp
                    traverse_node = traverse_node.link
                if traverse_node.data is not None and traverse_node.link is None:
                    if p.data > traverse_node.data:
                        temp = p.data
                        p.data = traverse_node.data
                        traverse_node.data = temp
                    traverse_node = traverse_node.link'''
            # if p.link is None and p.data is not None:


if __name__ == '__main__':
    SORT_LIST = SortList01()
    SORT_LIST.add_atend(9)
    SORT_LIST.add_atend(8)
    SORT_LIST.add_atend(7)
    SORT_LIST.add_atend(6)
    SORT_LIST.add_atend(5)
    SORT_LIST.add_atend(4)
    SORT_LIST.add_atend(3)
    SORT_LIST.add_atend(2)
    SORT_LIST.add_atend(1)

    SORT_LIST.display_list()

    print 'Number of elements in linked list is: ', SORT_LIST.count()

    SORT_LIST.bubble_sort()

    print 'Elements after bubble sort:'
    SORT_LIST.display_list()