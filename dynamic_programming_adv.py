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

  def maxProfit(self, prices):
    """
      Best time to buy and sell stock
      https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

      Say you have an array for which the ith element is the price of a
      given stock on day i.

      If you were only permitted to complete at most one transaction (i.e., buy
      one and sell one share of the stock), design an algorithm to find the
      maximum profit.

      Note that you cannot sell a stock before you buy one.

      Space - O(1) - constant number of variables
      Time - O(n) - where n is the number of items in prices.
      have to iterate over the entire prices array once
    """
    if prices == []: return 0
    # lowest possible profit. don't buy and sell anything
    curr_max_profit = 0

    # we checked for empty arr so there's there's at least 1 price
    curr_min_price = prices[0]

    # lowest possible profit. don't buy and sell anything
    curr_profit = 0

    for p in prices:
      # if current price is less than the current min
      # profit is going to be negative
      # eg: prices = [7,1],
      # when p == 1 curr_min = 7.
      # p < curr_min. profit will be 1-7 = -6 which is less than 0,
      # which is "don't buy or sell any stock"
      # so update min element. max_profit still stays the same
      curr_min_price = min(p, curr_min_price)

      # curr_profit = p - curr_min_price
      # if curr_profit > curr_max_profit we found a new profit
      # update curr_max_profit
      curr_max_profit = max(p - curr_min_price, curr_max_profit)

    return curr_max_profit

  def isSubsequence(self, s, t):
    """
    Is Subsequence
    https://leetcode.com/problems/is-subsequence/
    Given a string s and a string t, check if s is subsequence of t.

    A subsequence of a string is a new string which is formed from the
    original string by deleting some (can be none) of the characters without
    disturbing the relative positions of the remaining characters. (ie, "ace"
    is a subsequence of "abcde" while "aec" is not).

    O(1) space - two additional variables used
    O(n) time - where n is the length of string t or string s,
    whichever is longer
    Worst case, have to traverse the entire string t to see whether s is a
    subsequence of t
    Worst case, s is longer than t. calculating len(s) is O(n) time where
    n is length of s
    """

    if not s: return True
    s_idx = 0
    s_len = len(s)

    # traverse both strings
    # if the t char matches what we're looking for in the s char
    # increment s_idx
    # either way, increment t_idx so we can continue searching
    for t_idx in range(len(t)):
      if t[t_idx] == s[s_idx]:
        s_idx += 1
      if s_idx == s_len:
        return True

    return s_idx == s_len

d = DynamicProgrammingAdv()
assert d.rob([1,2,3,1]) == 4
assert d.rob([2,7,9,3,1]) == 12
assert d.rob([]) == 0
assert d.rob([3,5]) == 5
assert d.rob([5,3]) == 5
assert d.rob([3]) == 3

assert d.maxProfit([7,1,5,3,6,4]) == 5
assert d.maxProfit([7,6,4]) == 0
assert d.maxProfit([]) == 0
assert d.maxProfit([4]) == 0

assert d.isSubsequence("abc", "ahbgdc") == True
assert d.isSubsequence("axc", "xahbgdc") == False
assert d.isSubsequence("abc", "a") == False
assert d.isSubsequence("a", "c") == False
assert d.isSubsequence("abc", "abc") == True
assert d.isSubsequence("", "a") == True

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
