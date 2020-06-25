### Notes

### General

while i did manage to do the prework and am confident in my final answers, i'm
not confident about graphs in general. that is to say, given that there are so
many applications of graphs, even implementing something 'basic' like dfs or bfs
is quite daunting because of all the potential applications, constraints, and so
on. for example, i've read through the word search ladder and the knights tour a
few times and while i know those are bfs at the end of the day, i still haven't
managed to really 'get it' and implement those despite following along. i'm not
sure whether that means i don't understand dfs and bfs enough, or whether i need
more practice given the sheer amount of graph applications.

for what it's worth, i know that for...

### both searches
if the space to be searched is a graph, i need to keep track of the nodes that
have been visited to avoid checking nodes that have already been checked.
checking already-checked nodes is wasteful repeated work if the graph is
acyclic, and the search would never terminate if the graph is cyclic.

edges can have 'weights' - that is the cost to go from one node to the other.
for example, an edge can be the road between two locations. examples of th
edge's weight can include the distance between both locations and/or he cost to
travel that edge in terms of fuel and/oror time.

nodes frequently have information associated with them. this information is
called the 'payload'.

#### breadth-first search
generally used when you need to find the 'shortest path to something'. for
example, the shortest path from `a` to `b` on a map of roads, where the roads
are the edges and the places are the vertexes.

generally done iteratively

use a queue and append nodes. nodes are appended and searched by 'distance' from
the starting vertex. that is to say, the starting vertex will be checked first,
then all nodes directly connected to the starting vertex - let's call those
nodes `b`, then all nodes directly connected to  the `b` nodes, and so forth.

terminate when you find what you are looking for, or the queue is empty.

an empty queue means that all nodes have been searched.

#### depth-first search

generally used when you need to find the 'furthest you can go'. for example,
in the knights tour, you want to find out whether you can visit all 64 boxes in
a chessboard once. so you need to try to get a path of depth 64 that fulfils the
knight's tour criteria.

generally done recursively

from the starting vertex, pick an edge, and travel along that path until you
have reached the end of that path. the 'end' is a node that is not connected to
any other nodes or is only connected to nodes that have already been visited.
for example, let's say you visited nodes `[a,b,c,d]` in that order and `d` is
the 'end'. if you haven't found what you need at that end, travel 'backwards' to
the previous node - in this case, `c`. if `c` is connected to nodes you have not
yet visited, visit those. otherwise, back up to `b` and search there.

terminate when you find what you are looking for, or all nodes have been
visited.
