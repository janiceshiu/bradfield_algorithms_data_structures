import stack

class Queue:
  """
    Implement a queue using stacks
  """

  def __init__(self):
    self._items = stack.Stack()

  def enqueue(self, item):
    self._items.push(item)

  def dequeue(self):
    return self._items.pop()

  def is_empty(self):
    return self._items.is_empty()

  def size(self):
    return self._items.size()

q = Queue()
q.enqueue(2)
assert q.size() == 1
assert q.is_empty() == False
assert q.dequeue() == 2
assert q.is_empty() == True
assert q.size() == 0
