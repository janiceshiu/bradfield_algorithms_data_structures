## My questions from the reading
### Heap
* "In order to maintain the heap order property, all we need to do is swap the root with its smallest child less than the root." why the smallest child less than the root? what happens if we swap it with the larger child?
* Given the same list of numbers - will the binary heap list be exactly the same regardless of the order in which the numbers are inserted into the heap?
* "Although we start out in the middle of the tree and work our way back toward the root, the percolate_down method ensures that the largest child is always moved down the tree." I'm not sure what they mean by largest child. largest child of...?
### Binary Tree
* "A balanced binary tree has roughly the same number of nodes in the left and right subtrees of the root" why roughly?

## Prework questions
* What are the trade-offs being made between chaining and linear probing?
Linear probing - total memory size for the hash is allocated at the start
Tradeoff - clustering - if a lot of collisions occur around the same hash value, or there are are a few collisions that occur in an already densely-packed area of the hash table, then it degrades to sequential search where you search for the item until you either find it or you find an empty slot.
Chaining - if more than one item hashes to the same slot, make a list and append the item to the list. Advantage is that if the value hashes to slot X and you cannot find it in the list at slot X, it is definitely not there. disadvantage is that if everything hashes to the same value, then you get o(n) to search. degrades back to sequential search.
* Which of these do you think is more commonly used?
Not sure
* Considering a hash map that uses chaining, when should the underlying array grow? What about for one that uses linear probing?
When the load factor exceeds a certain amount. Not sure how much and when though. For arrays usually the principle is to double the space needed when the array is full.
