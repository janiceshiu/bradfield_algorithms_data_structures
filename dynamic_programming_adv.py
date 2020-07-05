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

