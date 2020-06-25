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
