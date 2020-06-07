### Reading
* [Stacks](https://bradfieldcs.com/algos/stacks/introduction/)
* [Queues](https://bradfieldcs.com/algos/queues/introduction/)
* [Dequeues](https://bradfieldcs.com/algos/deques/introduction/)

### Questions
1. What is the difference between an abstract data type and an implementation of a data structure?
* Abstract data type
  * We define the data type and the functions that can be done on the data type, as well as the resulting changes to the data type and what that function returns. However, we don't care how the functions and data type is implemented. For example, I might say that I want a Stack data type and is_empty() returns a boolean that indicates whether a stack is empty or not. As long as `stack.is_empty()` returns True on an empty stack and False on a non-empty stack, I don't care what language the stack is written in, what goes on and in the `is_empty` function.
* Implementation of a data structure
  * This is how the abstract data type is implemented. So for example, the Stack abstract data type is defined and `is_empty()` returns a boolean that indicates whether the stack is empty or not. Now, we need to care about how the stack is implemented, and how `is_empty` is implemented. For example, what language will we write the functions and the data type in? Within `is_empty`, how do I use my chosen programming langues to determine whether my stack is empty or not?

2. Consider two implementations of the queue abstract data type, one implemented using a dynamic array and the other as a doubly linked list. What is the Big O complexity of the push and pop operations? Other than Big O complexity, can you think of any potential performance differences between the two?
Time Complexity
|  | Dynamic Array | Doubly Linked List |
| --- | --- | --- |
| Push | o(1) amortized | o(1) |
| Pop | o(1) | o(1) |

Potential performance differences
* Need to update pointers for the doubly linked list. No need to update pointers for the dynamic array. Not sure how this affects performance
* If we want to view an item that is not at the start or the end of the queue, it is faster to do so in a dynamic array since lookup is o(1) time, whereas it is o(n) time in a doubly linked list.
* Dynamic array has items in contiguous memory. There might be a limit to how large this queue can become and the limit is the largest block of contiguous memory that the disk has. This limit could be lower on a very fragmented disk (memories of Windows 98 here) Doubly linked lists (and single linked lists) can store their contents all over a disk regardless of contiguous memory, and thus the queue size limit is probably higher.

### Coding
* [Stack implementation](stack.py)
* [Queue implementation using stacks](queue.py)
* [Function that uses a stack to return a reversed copy of  a list](reverse_list.py)
