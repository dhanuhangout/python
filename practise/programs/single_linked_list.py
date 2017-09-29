"""This module demonstrates single linked list."""

class node:
    def __init__(self):
        self.data = None
        self.next = None

class linked_list:
    def __init__(self):
        self.cur_node = None

    def add_node_atbegin(self, data):
        new_node = node()
        new_node.data = data
        new_node.next = self.cur_node
        self.cur_node = new_node

    def print_linkedlist(self):
        node = self.cur_node
        while node:
            print node.data
            node = node.next


ll = linked_list()
ll.add_node_atbegin(1)
ll.add_node_atbegin(2)
ll.add_node_atbegin(3)

ll.print_linkedlist()
