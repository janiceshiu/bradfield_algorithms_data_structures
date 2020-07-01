### Reading
* [Algos section on dynamic programming](https://bradfieldcs.com/algos/recursion/dynamic-programming/)

### Questions
1. In what scenarios can it be beneficial to apply dynamic programming?
When there is a lot of identical work being done over and over. For example, fib(5) is fib(4) + fib(3). But fib(4) itself is fib(3) + fib(2). If you draw out the table, you see that fib(3) gets computed multiple times, and fib(2) even more times. This is what leads to O(2^n) runtime for standard recursive fibonacci. However, if you store the result of fib(3) somewhere, you don't have to recalculate it, and you can bring the runtime down to O(n) runtime.

2. What are the differences between the memoization (top-down) and tabulation (bottom-up) approaches?
I'm not very sure. They both seem to be the same - storing some cache of solved problems.

3. Is there a relationship between the parameters of a recursive function and the corresponding memo table? What about between the time and space complexities of a top-down approach?
I really don't know this given that I'm not sure what the differences are between memoization and tabulation.
