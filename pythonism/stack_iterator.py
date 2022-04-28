class Stack:
  def __init__(self, collection=None):
    self.top = None
    self.size = 0
    if collection:
      for item in reversed(collection):
        self.push(item)
  
  def __iter__(self):
    def value_generator():
      current = self
      while current.top:
        yield current.pop()
    return value_generator()

  def __len__(self):
    return len(iter(self))

  def __eq__(self, other):
      return list(self) == list(other)

  def __getitem__(self, index):
      if index < 0:
          raise IndexError
      for i, item in enumerate(self):
          if i == index:
              return item
      raise IndexError

  def __str__(self):
      out = ''
      for value in self:
          out += f'[ {value } ] -> '
      out += 'None'
      return out

    
# STACK IMPLEMENTAION METHODS
  def push(self, value):
    new_node = Node(value)
    new_node.next = self.top
    self.top = new_node
    self.size += 1

  def pop(self):
    try:
      temp = self.top
      self.top = self.top.next
      self.size -= 1
      return temp.value
    except:
      if self.top == None:
        return Exception

  def peek(self):
    try:
      return self.top.value
    except:
      if self.top.value == None:
        return Exception

  def is_empty(self):
    return self.size == 0


# NODE CLASS IMPLEMENATION
class Node:
  def __init__(self, value, next_=None):
      self.value = value
      self.next = next_