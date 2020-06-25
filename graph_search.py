class GraphSearch:
  def dfs(self, target, graph, starting_vertex):
    info = {
      "target": target,
      "found": False,
      "visited": [],
      "checks_whether_vertex_is_target": 0
    }

    def traverse(vertex):
      info["visited"].append(vertex)
      info["checks_whether_vertex_is_target"] += 1
      if (vertex == target):
        info["found"] = True
        return info

      for v in graph[vertex]:
        if v not in info["visited"]:
          if traverse(v)["found"] == True:
            return info

      return info

    traverse(starting_vertex)
    return info

  def bfs(self, target, graph, starting_vertex):
    from collections import deque

    info = {
      "target": target,
      "found": False,
      "visited": [],
      "checks_whether_vertex_is_target": 0
    }

    queue = deque()
    queue.append(starting_vertex)

    while queue:
      vertex = queue.popleft()
      if vertex not in info["visited"]:
        info["checks_whether_vertex_is_target"] += 1
        info["visited"].append(vertex)

        if (vertex == target):
          info["found"] = True
          return info

      for v in graph[vertex]:
        if v not in info["visited"]:
          queue.append(v)

    return info

  def minimum_depth_of_binary_tree(self, root):
    """
    https://leetcode.com/problems/minimum-depth-of-binary-tree/
    Definition for a binary tree node.
    class TreeNode:
      def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

    The minimum depth is the number of nodes along the shortest path from
    the root node down to the nearest leaf node.

    Use breadth first search since you're finding the shortest path
    No need to take into account what has been visited since there is no
    cycle in a tree
    Take current level into account

    Solution
    Runtime: 44 ms, faster than 71.04% of Python3 online submissions.
    """

    if not root: return 0

    from collections import deque
    queue = deque()

    # root is at depth 1
    queue.append((root, 1))

    while queue:
      (node, depth) = queue.popleft()

      # found a leaf. return the current level
      if not node.left and not node.right:
        return depth

      # add the children. current level goes up by 1
      if node.left: queue.append((node.left, depth + 1))
      if node.right: queue.append((node.right, depth + 1))

simple_graph = {
    'A': ['B', 'D'],
    'B': ['C', 'D'],
    'C': [],
    'D': ['E'],
    'E': ['B', 'F'],
    'F': ['C']
}

g = GraphSearch()
assert g.dfs('T', simple_graph, 'A') == {'target': 'T', 'found': False, 'visited': ['A', 'B', 'C', 'D', 'E', 'F'], "checks_whether_vertex_is_target": 6}
assert g.dfs('F', simple_graph, 'A') == {'target': 'F', 'found': True, 'visited': ['A', 'B', 'C', 'D', 'E', 'F'], "checks_whether_vertex_is_target": 6}
assert g.dfs('C', simple_graph, 'A') == {'target': 'C', 'found': True, 'visited': ['A', 'B', 'C'], "checks_whether_vertex_is_target": 3}
assert g.dfs('A', simple_graph, 'A') == {'target': 'A', 'found': True, 'visited': ['A'], "checks_whether_vertex_is_target": 1}

assert g.bfs('T', simple_graph, 'A') == {'target': 'T', 'found': False, 'visited': ['A', 'B', 'D', 'C', 'E', 'F'], "checks_whether_vertex_is_target": 6}
assert g.bfs('F', simple_graph, 'A')  == {'target': 'F', 'found': True, 'visited': ['A', 'B', 'D', 'C', 'E', 'F'], "checks_whether_vertex_is_target": 6}
assert g.bfs('C', simple_graph, 'A') == {'target': 'C', 'found': True, 'visited': ['A', 'B', 'D', 'C'], "checks_whether_vertex_is_target": 4}
assert g.bfs('A', simple_graph, 'A') == {'target': 'A', 'found': True, 'visited': ['A'], "checks_whether_vertex_is_target": 1}
