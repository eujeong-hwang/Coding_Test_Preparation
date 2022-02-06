# Feb 06, 2022
## Question - 9. Palindrome Number
https://leetcode.com/problems/palindrome-number/

## What is a Palindrome Number?
    An integer is a palindrome when it reads the same backward as forward.

    For example, 121 is a palindrome while 123 is not.

## First Solution - Using Python
```
class Solution(object):
    def isPalindrome(self, x):
         if x > 0:
            temp = x
            rev_int_elements = []
            while temp > 0:
                digit = temp % 10
                rev_int_elements.append(digit)
                temp = temp // 10
            org_int_elements = rev_int_elements[::-1]
            return rev_int_elements == org_int_elements
        elif x == 0:
            return True
        else:
            return False
```

## Second Solution : Use less space

```
class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
```

## str(x)[::-1]

Example)

```
a = '1234'
a[::-1]

Output: 4321
```