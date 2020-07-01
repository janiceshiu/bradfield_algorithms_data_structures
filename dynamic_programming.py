class DynamicProgramming():
  def frog(self, n, stone_heights):
    """
      source: https://atcoder.jp/contests/dp/tasks/dp_a
      There are `n` stones, numbered 1,2,…,n.
      For each i (1≤i≤n), the height of Stone i is hi.
      A frog is on Stone 1 and is trying to reach Stone `n`

      If the frog is currently on Stone i , jump to Stone i+1 or Stone i+2.
      Here, a cost of |hi−hj| is incurred, where j is the stone to land on.

      Find the minimum possible total cost incurred before the frog reaches Stone `n`

      All values in input are integers.
      2 <= n <= 10^5
      1 <= hi <= 10^4
    """
    if n == 0 or n == 1:
      return 0
    if n == 2:
     return abs(stone_heights[1] - stone_heights[0])

    # make an array where cost[i] is the cost to reach stone i from stone 1
    # cost to reach the final stone, stone n, is cost_arr[-1]
    cost_arr = [0, abs(stone_heights[1] - stone_heights[0])]
    i = 2

    while i < n:
      cost_to_i_from_1_stone_before = abs(stone_heights[i] - stone_heights[i - 1])
      cost_to_i_from_2_stones_before = abs(stone_heights[i] - stone_heights[i - 2])

      if cost_to_i_from_2_stones_before + cost_arr[i - 2] <= cost_to_i_from_1_stone_before + cost_arr[i - 1]:
        cost_arr.append(cost_to_i_from_2_stones_before + cost_arr[i - 2])
      else:
        cost_arr.append(cost_to_i_from_1_stone_before + cost_arr[i - 1])

      i += 1

    print(cost_arr)
    return cost_arr[-1]

d = DynamicProgramming()

assert d.frog(0, []) == 0
assert d.frog(1, [2]) == 0
assert d.frog(2, [2,3]) == 1
assert d.frog(2, [3,2]) == 1
assert d.frog(2, [10, 10]) == 0
assert (d.frog(4, [10, 30, 40, 20])) == 30
assert d.frog(6, [30, 10, 60, 10, 60, 50]) == 40
