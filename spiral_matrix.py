class Solution:
  def spiral_order_recursive(self, matrix):
    """
      Given a matrix of m x n elements (m rows, n columns),
      return all elements of the matrix in spiral order
      https://leetcode.com/problems/spiral-matrix/
    """
    def do_spiral(matrix, acc):
      # base case of empty arr
      if matrix == []: return acc

      # # base case of [[1,2]]
      if len(matrix) == 1:
        for elem in matrix[0]:
          acc.append(elem)

        return acc
      max_idx = len(matrix) - 1

      # let's spiral across, down, and reverse across
      for idx, elem in enumerate(matrix):
        if idx == 0:
          for e in elem:
            acc.append(e)
        elif idx == max_idx:
          for e in reversed(elem):
            acc.append(e)
        else:
          acc.append(elem[-1])

      # if there is only one column it's already been used
      # bye we are done no spiraling up needed
      if len(matrix[0]) == 1: return acc

      # let's spiral up
      for idx, elem in enumerate(reversed(matrix)):
        if idx != 0 and idx != max_idx:
          acc.append(elem[0])

      # let's recurse
      # if only 2 columns, they've all been used. return acc
      if len(matrix[0]) == 2: return acc
      # if there is only one column it's already been used bye

      # let's make the matrix smaller for recursion
      # get rid of the first and last rows
      # they've already been used
      # note: slicing is expensive.
      # cos we are copying everything except for the outer ring.
      # optimization:
      # instead of slicing the matrix, keep track of indexes for
      # what regions of the matrix you're working with
      # keep track of top left (1,1) and bottom right (4,4)
      # top left increases by (1,1) bottom right decreases by (1,1)

      mtrx = matrix[1:-1]
      # get rid of the first and last items in the remaining lists
      # they've already been used
      for idx, elem in enumerate(mtrx):
        mtrx[idx] = elem[1:-1]

      return do_spiral(mtrx, acc)

    return do_spiral(matrix, [])

  def spiral_order_iterative(self):
    """
    solve this the iterative way

    plan:
    - keep track of where you're moving
    - if you're moving to the right, i, j i = row, j = column
    - changes by (0,1) (row stays same, column increases by 1) velocity is (0,1)
    - figure out velocity for all directions (0,1), (1,0), (0,-1), (-1,0)
    - keep moving. see whether it's a valid move. if it is, you move, if it's not, you turn
    - for loop that moves (n*m)-1 times cos you don't move on first step.
    - eg: matrix is 3 rows and 4 columns, 3x4 = 12. you move 11 times
    - keep track of coordinates you've already processed. eg: change item to nil. so if nil, turn
    """
    pass

class Test:
  def test(self):
    s = Solution()
    self.test_spiral_order(s)

  def test_spiral_order(self, s):
    matrices = [
      [],
      [[1,2]],
      [[1,2], [3,4]],
      [[1,2], [3,4], [5,6]],
      [[1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12]],
      [[7], [9], [6]],
      [[1,11], [2,12], [3,13], [4,14], [5,15], [6,16], [7,17], [8,18], [9,19], [10,20]],
      [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    ]

    expected_results = [
      [],
      [1,2],
      [1,2,4,3],
      [1,2,4,6,5,3],
      [1,2,3,4,8,12,11,10,9,5,6,7],
      [7,9,6],
      [1,11,12,13,14,15,16,17,18,19,20,10,9,8,7,6,5,4,3,2],
      [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
    ]

    for idx, m in enumerate(matrices):
      try:
        result = s.spiral_order_recursive(m)
        assert result == expected_results[idx]
      except AssertionError:
        print(m)
        print(result)
        print(expected_results[idx])

t = Test()
t.test()
