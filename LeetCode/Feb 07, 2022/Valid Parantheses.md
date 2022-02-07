# Feb 07, 2022
## Question - 20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

## Related Topics
    String
    Stack

## Solution - Using Python
```
class Solution(object):
    def isValid(self, s):
        stack=[]
        brackets={'}':'{',')':'(',']':'['}
        for bracket in s:
            #Opening bracket 
            if bracket in brackets.values():
                stack.append(bracket)
            # Closing bracket
            else:
                if stack and brackets[bracket]==stack[-1] :  
                    stack.pop()
                else: 
                    return False
        if stack:
            return False
        return True
```

## What is Stack in Python?

1. A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner.

2. Stack in Python can be implemented using the following ways: 
    - list
    - Collections.deque
    - queue.LifoQueue

3. Python’s built-in data structure **list** can be used as a stack.
    - append()
    - pop()

Reference: https://www.geeksforgeeks.org/stack-in-python/


## What I learned 

1. 
```
stack = [1, 3, 5, 6, 1]
# x[-1] returns the last element of the list
stack[-1] = 1
stack[-2] = 6
```
