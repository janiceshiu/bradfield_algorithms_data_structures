import stack

class ReverseList:
  @staticmethod
  def reverse(l):
    """
      Write a function that uses a stack to return a reversed copy of a list.

      Analysis:
      Time - o(n) - need to access each item once
      Space - o(n) - need to make another copy of the list, this time stored in stack's items
      n is the length of the list `l`
    """
    s = stack.Stack()

    while l != []:
      s.push(l.pop())

    return s._items

assert ReverseList.reverse([1,2,3,4,5]) == [5,4,3,2,1]
