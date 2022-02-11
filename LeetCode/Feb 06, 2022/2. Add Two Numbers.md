# Feb 06, 2022
## Question - 2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

## Related Topics
    Linked List
    Math
    Recursion

## Solution - Using Python (Not Python3)

- What is Linked List?

https://github.com/eujeong-hwang/Coding_Test_Preparation/blob/main/Concepts/Data%20Structure/Linked%20List.md

## First Solution: Using Singly Linked-List

```
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
  def addTwoNumbers(self, l1, l2):
        carry = 0;
        res = n = ListNode(0);
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next;
            if l2:
                carry += l2.val;
                l2 = l2.next;
            carry, val = divmod(carry, 10)
            n.next = n = ListNode(val);
        return res.next;
```

## Something I learned while solving this problem
- Ternary conditional operator

First, condition is evaluated, then if condition evaluated to true, then a is returned, 
or else, b is returned

```
a if condition else b
```

- divmod()

The divmod() method takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.

If x and y are integers, the return value from divmod() is same as (a // b, x % y).

```
divmod(x, y)
```

## Reference
https://www.youtube.com/watch?v=wgFPrzTjm7s