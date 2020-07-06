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
