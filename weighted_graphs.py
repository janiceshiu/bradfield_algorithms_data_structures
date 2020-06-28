class WeightedGraphs():
  def dijkstras_algorithm(self, graph, starting_vertex):
    """
      my implementation and understanding is heavily taken from bradfield's
      article https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/ and
      Bari's video https://www.youtube.com/watch?v=XB4MIexjvY0

      I've commented almost every line of the function and printed a whole
      bunch of info so that it is much more obvious to me how the algorithm
      runs, especially the part about updating the dict of costs

      Note that I put 'cost' rather than 'distance' to make this more generic
      because at the end of the day, a weighted graph just says that oh, it
      takes X to go from Y to Z. and that X can be distance, time, etc.
      at the end of the day, X is just a cost.
    """

    import pprint
    # pp = pprint.PrettyPrinter(indent=2)
    pprint.pprint(graph)
    # let's say (source_vertex, target_vertex, distance) and we have
    # [(a, b, 5), (a, c, 7), (c, d, 3)]

    # cost_to_starting_vertex == costs_to_start_vert
    # initialise the dict.
    # for vertex in graph, set the distance from the starting vertex to infinity
    costs_to_start_vert = {vertex: float('infinity') for vertex in graph}

    # obviously, the distance from the starting vertex to itself is 0. so update that
    costs_to_start_vert[starting_vertex] = 0

    # dist_frm_start_vert == {'a': 0, 'b': inf, 'c': inf, 'd': inf}

    import heapq
    # priority queue time

    # we process vertexes that have the lowest weight to starting_vertex,
    # and that are directly connected to starting_vertex
    # process vertex `a` first.
    # `b` and `c` are directly connected to `a`, so process them next
    # `b` is weight 5 to `a`. `c` is weight 7. so process vertex `b` first
    # and so on.

    # let's go. initialise the priority queue with (0, starting_vertex)
    # makes sense cos hey, starting_vertex is a weight of 0 to itself
    priority_queue = [(0, starting_vertex)]

    # while the queue isn't empty...
    while priority_queue:
      # pop the top of the heap off. this is the vertex with the lowest weight to the starting_vertex
      curr_cost_to_start_vert, curr_vert = heapq.heappop(priority_queue)
      print(f"**curr_vert {curr_vert}**")
      print(f"existing_cost_to_{starting_vertex}: {costs_to_start_vert[curr_vert]}. costs_to_{starting_vertex}: {costs_to_start_vert}")

      # note says "nodes can get added to the priority queue many times
      # only process a vertex the first time we remove it from the priority queue"
      # ^ not sure what that means and why it's important we do this
      # not terribly sure why curr_cost_to_start_vert might be more than
      # costs_to_start_vert[curr_vert]
      if curr_cost_to_start_vert > costs_to_start_vert[curr_vert]:
        print(f"curr_cost_to_start_vert: {curr_cost_to_start_vert} > costs_to_start_vert[curr_vert]: {costs_to_start_vert[curr_vert]}, curr_vert: {curr_vert}")
        continue

      vertexes_directly_connected_to_curr_vert = [vertex for vertex, _cost in graph[curr_vert].items()]
      print(f"{curr_vert} is connected to {vertexes_directly_connected_to_curr_vert}")
      # neighbour vertex means a vertex that is directly connected to our current vertex
      for neighbour_vertex, cost in graph[curr_vert].items():
        # let's say it cost `7` to get to vertex `c`
        # `c` is directly connected to `d` and the cost of c -> d is 3
        # so proposed_cost to go from start_vert to `d` == 7 +3 == 10
        proposed_cost = curr_cost_to_start_vert + cost

        if proposed_cost < costs_to_start_vert[neighbour_vertex]:
        # found a shorter path to this neighbour_vertex! update the dict!
          print(f"from {starting_vertex} to {neighbour_vertex}, proposed cost {proposed_cost} < current cost {costs_to_start_vert[neighbour_vertex]}. update dict")
          costs_to_start_vert[neighbour_vertex] = proposed_cost

          # add this to the priority queue
          heapq.heappush(priority_queue, (proposed_cost, neighbour_vertex))

        else:
          print(f"from {starting_vertex} to {neighbour_vertex}, proposed cost {proposed_cost} >= current cost {costs_to_start_vert[neighbour_vertex]}. don't update dict")

        print(f"processed neighbour vertex {neighbour_vertex}. costs_to_{starting_vertex}: {costs_to_start_vert})\n")

    print(f"\n**ending**\nfinal costs to each vertex from vertex {starting_vertex}: {costs_to_start_vert}")
    print(f"original graph: {graph}")
    return costs_to_start_vert

  def network_delay_time(self, times, N, K):
    """
      from https://leetcode.com/problems/network-delay-time/
      There are N network nodes, labelled 1 to N.

      Given times, a list of travel times as directed edges
      times[i] = (u, v, w), where u is the source node, v is the target node,
      and w is the time it takes for a signal to travel from source to target.

      Now, we send a signal from a certain node K.

      How long will it take for all nodes to receive the signal?
      If it is impossible, return -1.

      times: List[List[int]], N: int, K: int) -> int:

      Example
      Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
      Output: 2

      Runtime: 496 ms, faster than 73.14% of Python3 online submissions
      for Network Delay Time.
      Memory Usage: 15.8 MB, less than 19.89% of Python3 online submissions
      for Network Delay Time.
    """
    # if impossible, return -1
    # bfs. if not all are connected, impossible. return -1

    from collections import defaultdict, deque
    # defaultdict so we don't have to handle keyerror
    # dequeue so queueing and dequeueing is o(1) time
    graph = defaultdict(list)

    # build graph
    for source, target, time in times:
      graph[source].append((target, time))

    # check whether possible
    visited_nodes = set()

    queue = deque()
    queue.append(K)

    while queue:
      node = queue.popleft()
      if node not in visited_nodes:
        visited_nodes.add(node)
        for target_node, _time in graph[node]:
          queue.append(target_node)

    if len(visited_nodes) != N: return -1

    # ok visiting all is possible now to see how long all nodes take to receive the signal
    # dijikstra probably. and then just take... the node with the largest time from node K
    # that should be the max length for that node to receive the signal

    # dijkstra time
    # for vertex in graph, set the distance from the starting vertex to infinit
    travel_time_from_start_vert = {vertex: float('infinity') for vertex in graph}

    # K is the starting node
    travel_time_from_start_vert[K] = 0

    # priority queue time
    import heapq

    priority_queue = [(0, K)]

    while priority_queue:
      curr_time_to_start_vert, curr_vert = heapq.heappop(priority_queue)


      if curr_time_to_start_vert > travel_time_from_start_vert[curr_vert]:
        continue

      for neighbour_vertex, time in graph[curr_vert]:
        proposed_time = curr_time_to_start_vert + time
        if proposed_time < travel_time_from_start_vert[neighbour_vertex]:
          travel_time_from_start_vert[neighbour_vertex] = proposed_time

          heapq.heappush(priority_queue, (proposed_time, neighbour_vertex))

    # get the keys of the final dict from dijkstra's.
    # the node with the largest time from node K
    # should be the max length for that node to receive the signal
    return max(travel_time_from_start_vert.values())

example_graph = {
  'U': {'V': 2, 'W': 5, 'X': 1},
  'V': {'U': 2, 'X': 2, 'W': 3},
  'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
  'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
  'Y': {'X': 1, 'W': 1, 'Z': 1},
  'Z': {'W': 5, 'Y': 1},
}

w = WeightedGraphs()
w.dijkstras_algorithm(example_graph, 'U')

# test cases from leetcode. i modified one to test for -1
assert w.network_delay_time([[1,2,1],[2,1,3]], 2, 2) == 3
assert w.network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2
assert w.network_delay_time([[2,1,1],[3,4,1]], 4, 2) == -1
