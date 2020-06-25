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

