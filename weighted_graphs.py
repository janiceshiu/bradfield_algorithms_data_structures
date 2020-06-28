class WeightedGraphs():
  def dijkstras_algorithm(self, graph, starting_vertex):
    """
    my implementation and understanding is heavily taken from bradfield's article
    https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/ and Bari's video
    https://www.youtube.com/watch?v=XB4MIexjvY0

    I've commented almost every line of the function and printed a whole bunch
    of info so that it is much more obvious to me how the algorithm runs,
    especially the part about updating the dict of costs

    Note that I put 'cost' rather than 'distance' to make this more generic
    because at the end of the day, a weighted graph just says that oh, it takes
    X to go from Y to Z. and that X can be distance, time, etc. at the end of
    the day, X is just a cost.
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
