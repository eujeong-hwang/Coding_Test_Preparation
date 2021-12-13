# Dynamic programming

- Dynamic programming is breaking down a problem into smaller sub-problems, solving each sub-problem and storing the solutions to each of these sub-problems in an array (or similar data structure) so each sub-problem is only calculated once.
- An optimization over plain recursion
- Avoiding the work of recomputing the answer every time the subproblem is encountered.
- The idea is to simply store the results of subproblems, so that we do not have to re-compute them when needed later. 

<br>

# Divide & Conquer Algorithm vs. Dynamic Programming

- Divide and Conquer Algorithm
    Divide and conquer algorithms partition the problem into independent sub-problems to solve the sub-problems recursively and then combine their solutions to solve the original problem.

- Dynamic Programming
    Dynamic programming is applicable when the sub-problem is not independent, that is when sub-problems share sub-problems. Therefore, a dynamic programming algorithm solves every sub-problem just once and then saves its answers in a table, thereby avoiding the work of recomputing the answer every time the subproblem is encountered. Dynamic programming has an extra step compared to Divide & Conquer Algorithm, which is MEMOISATION. 

<br>

# Memoisation

In Dynamic Programming we store the solution to the problem so we do not need to recalculate it. By finding the solutions for every single sub-problem, we can tackle the original problem itself. And we call it "Memoisation", in this case, the act of storing a solution. 

<br>

# Python Examples of Dynamic Programming: Fibonacci Sequence


# Reference
https://favtutor.com/blogs/dynamic-programming
https://skerritt.blog/dynamic-programming/