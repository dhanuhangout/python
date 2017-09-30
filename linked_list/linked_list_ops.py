
class Node:
  def __init__(self):
    self.data = None
    self.link = None

class LinkedList:
  def __init__(self):
    self.node = Node()

  def add_atbegin(self, num):
    temp = Node()
    temp.data = num
    temp.link = self.node
    self.node = temp

  def add_atend(self, num):
    temp = Node()
    r = Node()
    if self.node.data == None:
      temp.data = num
      self.node = temp
    else:
      temp = self.node
      while temp.link != None:
        temp = temp.link
      r.data = num
      temp.link = r

  def add_after(self, loc, num):
    temp = Node()
    r = Node()
    temp = self.node
    for i in range(loc):
      temp = temp.link
      if temp.data is None and temp.link is None:
        print 'There are less than %d elements in list' % loc
        return
    r.link = temp.link
    r.data = num
    temp.link = r

  def delete(self, num):
    old = Node()
    temp = Node()
    temp = self.node
    while temp.link != None:
      if temp.data == num:
        if temp == self.node:
          self.node = temp.link
        else:
          old.link = temp.link
        return
      else:
        old = temp
        temp = temp.link
    # If the element to be deleted is the last element.
    if temp.data == num and temp.link == None:
      old.link = temp.link
      return
    print 'Element %d not found' % num

  def display(self):
    '''Display all nodes present in linked list.'''
    print 'Contents of linked list are:'
    temp = self.node
    # print self.node.data, self.node.link
    while temp.link != None: # TODO: Change it to while node.link != None:
      print temp.data
      temp = temp.link
    # If the list index reaches last node or list contains only one node.
    if temp.data != None and temp.link == None:
      print temp.data

  def count(self):
    print 'Returns count of number of nodes present in list.'
    c = 0
    temp = self.node
    while temp.link != None:
      temp = temp.link
      c += 1
    return c+1  # +1 is to add Last node of the list.


if __name__ == '__main__':
  p = LinkedList()
  print 'Number of elements in the linked list = ', p.count()
  
  p.add_atend(14)
  p.add_atend(30)
  p.add_atend(25)
  p.add_atend(42)
  p.add_atend(17)

  p.display()

  p.add_atbegin(999)
  p.add_atbegin(888)
  p.add_atbegin(777)

  p.display()

  p.add_after(7, 0)
  p.add_after(2, 1)
  p.add_after(5, 99)

  p.display()
  print 'Number of elements in the linked list = ', p.count()

  p.delete(99)
  p.delete(1)
  p.delete(10)
  p.delete(777)
  p.delete(0)

  p.display()
  print 'Number of elements in the linked list = ', p.count()
