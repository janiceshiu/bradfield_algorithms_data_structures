### Prework
* Read [shortest path](https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/) in /algos
* Read [this article](https://www.redblobgames.com/pathfinding/a-star/introduction.html) about BFS, DFS, Dijkstra’s Algorithm and the two heuristic based search algorithms “best first” (greedy) search and A*.

### Questions
1. What exactly are the differences between each of the algorithms?
* Already covered the difference between BFS and DFS in an earlier class, so I'll talk more about BFS, Dijkstra's, "best first" and A*
* BFS is the general breadth first search algorithm. It assumes the cost to move from one vertex to another is always the same.
* Dijkstra's is BFS that allows us to different costs to move to different vertexes. So for example, we can say a -> b costs 2 and a -> c costs 3 and Dijkstra's can take that into account and find the least costly path from one vertex to another.

2. To what kind of problems they may apply?
* Generally all apply to pathfinding problems. And pathfinding problems can be used in all sorts of things - from finding how to go from one location to another real-world location, to games maps, to packets jumping all over the network all over the world, and to anything that can be represented as a graph with some sort of possibly variable cost to go from vertex to vertex.

3. Where might you prefer one over another?
* When you want to find the path from one vertex to all other vertexes, or to most of those vertexes...
  * BFS when cost from one vertex to another is constant and you just want to find the shortest path, or to check that all vertices are connected. Note that in this case, the shortest path is also the least costly path since cost from one vertex to another is constant.
  * Dijkstra's when cost from one vertex to another is constant and you just want to find the least costly path, or the lowest cost from the starting vertex to every other vertex.
* When you want to find the path from one vertex to just one other vertex...
  * "Best first" when your graph is representing something like a map and there aren't many obstacles in the map.
  * A* when your graph is representing something like a map and there are a lot of obstacles in the map.
* A* is the 'best of both worlds' in that it is faster than BFS like "best first" and finds the shortest path like BFS because "best first" doesn't always find the shortest path.
* Not sure why "best first" runs faster than BFS even though BFS finds the more optimal path. There wasn't time complexity analysis in the [article](https://www.redblobgames.com/pathfinding/a-star/introduction.html)

### Notes
* Took me quite a while to get Dijkstra's and I had to rewrite the algorithm presented in [shortest path](https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/) with my own variable names, a ton of comments, and a ton of prints for me to see how the graph was first initialised, and how it changed with each step in the algorithm
* I still don't get the implementation of "best first" and A*, but I haven't yet re-implemented them with a ton of comments. Maybe it'll come to me then. Getting through Dijkstra's and Network Delay Time fried my brain
* There is probably a better solution for Network Delay Time given I'm only in the top ~27% of solutions. Haven't managed to think of a better one, though. I did wonder whether there was a way to get the graph built more efficiently before running Dijkstra on it, but I'm not sure.
