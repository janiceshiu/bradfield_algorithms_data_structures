class Frog():
  """
    source: https://atcoder.jp/contests/dp/tasks/dp_a
    There are `n` stones, numbered 1,2,…,n.
    For each i (1≤i≤n), the height of Stone i is hi.
    A frog is on Stone 1 and is trying to reach Stone `n`

    If the frog is currently on Stone i , jump to Stone i+1 or Stone i+2.
    Here, a cost of |hi−hj| is incurred, where j is the stone to land on.

    Find the minimum possible total cost incurred before the frog reaches
    stone `n`

    All values in input are integers.
    2 <= n <= 10^5
    1 <= hi <= 10^4

    Note:
    Using dynamic programming, this can be solved in 4 different ways
    1. iterative solution. start with calculating the total cost to reach
    stone i from the first stone. this means iterating over the array from
    idx 0 to idx n-1.
    2. iterative solution. start with calculating the total cost to reach
    stone i from the first stone. this means iterating over the array from
    idx 0 to idx n-1.
    3. recursive solution. start with calculating the total cost to reach
    stone n from the n-1th stone. this means iterating over the array from
    idx n-1 to idx 0.
    4. recursive solution. start with calculating the total cost to reach
    stone n from the n-1th stone. this means iterating over the array from
    idx n-1 to idx 0.
  """

  def front_to_back_iterative(self, n, h):
    """
      `cost` is the minimum cost to jump from the first stone (at index 0) to
      a stone at index `i`.

      cost[0] == 0 because there is no cost to jump from stone 0 to stone 0
      cost[n-1] is what we are looking for - the minimum cost to jump from
      stone 0 to the last stone
    """
    if n == 0 or n == 1: return 0

    # earlier check means by this point, there are at least 2 items in the array
    # set the FIRST 2 items in the cost array so that in the for loop, we know
    # that when we 'look BACK' at the values, they are already calculated.
    # eg: to calculate `cost[i]`, we look at `cost[i-1]` and `cost[i-2]`
    # to see whether jumping from the first stone to stone `i` is cheaper FROM
    # stone `i-1` or FROM stone `i-2`
    cost = [0] * n
    cost[1] = abs(h[1] - h[0])

    for i in range(2, n):
      # small jump means the total cost to jump from the
      # first stone - stone `0` to stone `i`
      # where the LAST JUMP is from stone `i-1` to stone `i`
      small_jump = cost[i-1] + abs(h[i] - h[i-1])

      # big jump means the total cost to jump from the
      # first stone - stone `0` to stone `i`
      # where the LAST JUMP is from stone `i-2` to stone `i`
      big_jump = cost[i-2] + abs(h[i] - h[i-2])

      # min cost to jump from stone 0 to stone `i` is whichever cost is lower
      cost[i] = min(small_jump, big_jump)

    print(f"min cost to jump from stone[0] to stone[i]: {cost}")
    return cost[-1]

  def back_to_front_iterative(self, n, h):
    """
      `cost` is the minimum cost to jump from a stone at index `i` to the last
      stone, which is at index `n-1`

      `cost[n-1]` is 0 because there is no cost to jump from the last stone at
      index n-1 to the exact same last stone.
      `cost[0]` is what we want - the minimum cost to jump from the first stone
      at index 0 to the last stone at index n-1
    """
    if n == 0 or n == 1:
      return 0

    # earlier check means by this point, there are at least 2 items in the array
    # set the LAST 2 items in the cost array so that in the for loop, we know
    # that when we 'look FORWARD' at the values, they are already calculated.
    # eg: to calculate `cost[i]``, we look at `cost[i+1]` and `cost[i+2]`
    # to see whether jumping from stone `i` to stone `n` is cheaper VIA
    # stone `i+1` or VIA stone `i+2`
    cost = [0] * n
    cost[-2] = abs(h[-1] - h[-2])

    for i in range(n-3, -1, -1):
      # small jump means the total cost to jump from
      # stone i to the last stone - stone `n-1`,
      # where the FIRST JUMP is from stone `i` to stone `i+1`
      small_jump = cost[i+1] + abs(h[i+1] - h[i])

      # big jump means the total cost to jump from
      # stone i to the last stone - stone `n-1`,
      # where the FIRST JUMP is from stone `i` to stone `i+2`
      big_jump = cost[i+2] + abs(h[i+2] - h[i])

      cost[i] = min(small_jump, big_jump)

    print(f"min cost to jump from stone[i] to stone[n-1]: {cost}")
    return cost[0]

  def frog_front_to_back_recursive(self, n, h):
    if n == 0 or n == 1: return 0

    # set up the memo
    # `None` means we haven't populated the memo at that index
    cost = [None] * n
    cost[0] = 0
    cost[1] = abs(h[1] - h[0])

    def min_cost_from_start_to_stone_i(i):
      # base cases
      if i == 0: return cost[0]
      if i == 1: return cost[1]

      # check whether the memo contains a previously calculated result
      if cost[i] != None: return cost[i]
      small_jump = min_cost_from_start_to_stone_i(i-1) + abs(h[i] - h[i-1])

      big_jump = min_cost_from_start_to_stone_i(i-2) + abs(h[i] - h[i-2])

      # since we had to do calculations to reach this point, save the result
      # to memo so that it is not recalculated the next time
      # min_cost_from_start_to_stone_i(i) is called
      cost[i] = min(small_jump, big_jump)
      return cost[i]

    min_cost = min_cost_from_start_to_stone_i(n-1)
    print(f"min cost to jump from stone[i] to stone[n-1]: {cost}")
    return min_cost

f = Frog()

# Both front_to_back_iterative and front_to_back_recursive should calculate
# the same cost array - the min cost to jump from stone[0] to stone[i].
# They are operating on the same principle.
# The only difference is one is iterative and one is recursive
print("front to back iterative")
assert f.front_to_back_iterative(0, []) == 0
assert f.front_to_back_iterative(1, [2]) == 0
assert f.front_to_back_iterative(2, [2,3]) == 1
assert f.front_to_back_iterative(2, [3,2]) == 1
assert f.front_to_back_iterative(2, [10, 10]) == 0
assert f.front_to_back_iterative(4, [10, 30, 40, 20]) == 30
assert f.front_to_back_iterative(6, [30, 10, 60, 10, 60, 50]) == 40
print("\n")

print("front to back recursive")
assert f.frog_front_to_back_recursive(0, []) == 0
assert f.frog_front_to_back_recursive(1, [2]) == 0
assert f.frog_front_to_back_recursive(2, [2,3]) == 1
assert f.frog_front_to_back_recursive(2, [3,2]) == 1
assert f.frog_front_to_back_recursive(2, [10, 10]) == 0
assert f.frog_front_to_back_recursive(4, [10, 30, 40, 20]) == 30
assert f.frog_front_to_back_recursive(6, [30, 10, 60, 10, 60, 50]) == 40
print("\n")

# Both back_to_front_iterative and frog_back_to_front_recursive should calculate
# the same cost array - the min cost to jump from stone[i] to stone[n-1].
# They are operating on the same principle.
# The only difference is one is iterative and one is recursive
print("back to front iterative")
assert f.back_to_front_iterative(0, []) == 0
assert f.back_to_front_iterative(1, [2]) == 0
assert f.back_to_front_iterative(2, [2,3]) == 1
assert f.back_to_front_iterative(2, [3,2]) == 1
assert f.back_to_front_iterative(2, [10, 10]) == 0
assert f.back_to_front_iterative(4, [10, 30, 40, 20]) == 30
assert f.back_to_front_iterative(6, [30, 10, 60, 10, 60, 50]) == 40
print("\n")

