class DynamicProgrammingAdv():
  def rob(self, nums):
    """
      House Robber
      https://leetcode.com/problems/house-robber/

      You are a professional robber planning to rob houses along a street.
      Each house has a certain amount of money stashed, the only constraint
      stopping you from robbing each of them is that adjacent houses have
      security system connected and it will automatically contact the police
      if two adjacent houses were broken into on the same night.

      Given a list of non-negative integers representing the amount of money
      of each house, determine the maximum amount of money you can rob tonight
      without alerting the police.

      0 <= nums.length <= 100
      0 <= nums[i] <= 400

      o(n) space.
      could probably be done in o(1) space cos you only need to take into
      account the amount you can get from robbing idx-2 and idx-1.
      tried it but it was way more confusing and i didn't manage to solve it.
      o(n) time
    """

    nums_length = len(nums)

    # handle cases where there are less than 2 houses
    # cos in these cases, no skipping required
    if nums_length == 0: return 0
    if nums_length == 1: return nums[0]

    # there are at least 2 houses. solve this case first
    # rob_at_idx is the max amount of money you can get if you only robbed from
    # nums[0] to nums[idx]
    rob_at_idx = [nums[0], max(nums[0], nums[1])]

    # iterate and check whether it's more worth it to rob or to skip
    for n in range(2, nums_length):
      rob_n = rob_at_idx[n-2] + nums[n]
      skip_n = rob_at_idx[n-1]
      rob_at_idx.append(max(rob_n, skip_n))

    return rob_at_idx[-1]

d = DynamicProgrammingAdv()
assert d.rob([1,2,3,1]) == 4
assert d.rob([2,7,9,3,1]) == 12
assert d.rob([]) == 0
assert d.rob([3,5]) == 5
assert d.rob([5,3]) == 5
assert d.rob([3]) == 3

class NumArray:
    def __init__(self, nums):
      """
      range sum query - immutable
      https://leetcode.com/problems/range-sum-query-immutable/
      Given an integer array nums, find the sum of the elements between
      indices i and j (i ≤ j), inclusive.

      dummy value 0 at the start. doesn't affect sum
      but means that sum from i to j inclusive is
      sum at j+1 - sum at i
      nums = [-2, 0, 3, -5, 2, -1]
      self.cache = [0, -2, -2, 1, -4, -2, -3]

      sumRange(i=0,j=2) == sum of [-2, 0, 3] == 1
      that is self.cache[j+1] - self.cache[i] aka self.cache[2+1] - self.cache[0]

      sumRange(i=2,j=5) == sum of [3, -5, 2, -1] == -1
      that is self.cache[5+1] - self.cache[2] = -3 -(-2) = -1

      init is o(n) space to store the cache. o(n) time to create the cache

      but calls to sumRange are o(1) time cos it's just accessing the array
      twice and doing subtraction
      """
      self.cache = [0]

      for idx in range(0, len(nums)):
        self.cache.append(nums[idx] + self.cache[idx])

    def sumRange(self, i, j):
        return self.cache[j+1] - self.cache[i]

obj = NumArray([-2, 0, 3, -5, 2, -1])
assert obj.sumRange(0, 2) == 1
assert obj.sumRange(2,5) == -1
assert obj.sumRange(0, 5) == -3

obj = NumArray([])
obj = NumArray([1])
assert obj.sumRange(0,0) == 1
