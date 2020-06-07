class Stack:
  def __init__(self):
    """
      time & space - o(1)
    """
    self._items = []

  def push(self, item):
    """
      time & space - o(1)
    """
    self._items.append(item)

  def pop(self):
    """
      time - o(1)
    """
    return self._items.pop()

  def peek(self):
    """
      time - o(1)
    """
    return self._items[-1]

  def is_empty(self):
    """
      o(1) time? not sure
    """
    return self._items == []

  def size(self):
    """
      o(n) time
    """
    return len(self._items)

s = Stack()
s.push(2)
assert s.size() == 1
assert s.is_empty() == False
assert s.peek() == 2
assert s.pop() == 2
assert s.is_empty() == True
assert s.size() == 0
