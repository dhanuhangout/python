def binary_tree(root):
  return [ root, [], [] ]

def insert_left(root, new_branch):
  temp = root.pop(1) # Pop out left node of root node.
  # Insert new list into the second position of root list.
  # If the list already has something in the second position, push it down the
  # tree as the left child of the list we are adding.
  if len(temp) > 1:
    root.insert(1, [new_branch, temp, []] )
  else:
    root.insert(1, [new_branch, [], []] )
  return root

def insert_right(root, new_branch):
  temp = root.pop(2)
  if len(temp) > 1:
    root.insert(2, [new_branch, [], temp] )
  else:
    root.insert(2, [new_branch, [], []] )
  return root

def get_root_val(root):
  return root[0]

def set_root_val(root, new_val):
  root[0] = new_val

def get_right_child(root):
  return root[2]

def get_left_child(root):
  return root[1]


root = binary_tree(3)
insert_left(root, 4)
insert_left(root, 5)
insert_right(root, 6)
insert_right(root, 7)
li = get_left_child(root)
print(li)

# set_root_val(1, 9)
#print(root)

#insert_left(1, 11)
#print(root)

print(get_right_child(get_right_child(root)))
