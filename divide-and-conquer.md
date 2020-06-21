## Prework
### Resources
* [Sorting algorithms](http://introcs.cs.luc.edu/arrays/sorting.html)
* [Visualisation tool](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html)

### Questions
* For each of bubble, insertion, and selection sort, what are the best and worse case scenarios?
Bubble sort
Best case - o(n) time. array already sorted
Worst case - o(n^2) time. array is completely reversed. The first element
from the unsorted array is the largest element. Since the array is completely
reversed, to 'bubble' it to the top, you not only have to compare this item to
every item in the unsorted array, you also have to swap this item with every item
in the unsorted array. That also takes time.

Selection sort
Best case & worst case - o(n^2) time regardless of how the items are arranged
This is because every time, you are going through the entire unsorted array to
find the smallest item. Then, you put that item at the end of the sorted array.
Unlike insertion and bubble sort, the algorithm doesn't even check whether the
array is already sorted.

Insertion sort
Best case - o(n) time. array is already sorted.
Worst case - o(n^2) time. array is completely reversed.
You have to compare the current item, which is smaller than every item in the
existing sorted array, to every item in the array before you find the position
to insert it in... which is at the start of the array.

* Why is the sorting problem a good candidate for divide and conquer?
You can sort smaller lists individually and then combine those sorted lists to
make it into a giant sorted list. And you can do that with really large lists
cos you can split those lists into smaller lists that fit in memory, sort
these, and then take the pointers to those lists and sort them the way we did
with that in-class exercise where you take n pointers to n sorted heaps and
return a list of the top X items.

* Other questions
It would be nice to briefly discuss how these algorithms are used on real-world
data. One example that comes to mind is [timsort](https://en.wikipedia.org/wiki/Timsort)
which is used in Python. I read through the wikipedia page but am still not
very clear on how 'natural runs' in data help this algorithm to run faster
than merge sort in certain cases. By faster I mean that while the algorithm
might still be in n log n time in terms of big o, the constants might be smaller
and thus in the 'real world' it would still run faster than merge sort. Merge
sort, as I understand it, is always n log n for best, worst, and average cases.
However, with timsort, you could get somewhere between n, where the data is
already sorted, and n log n, which is merge sort's invariant runtime. Thanks!
