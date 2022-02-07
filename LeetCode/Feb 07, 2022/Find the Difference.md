# Feb 07, 2022
## Question - 389. Find the Difference
https://leetcode.com/problems/find-the-difference/

## Related Topics
    Hash Table
    String
    Bit Manipulation
    Sorting

## Solution 1 - Using Python
```
class Solution(object):
    def findTheDifference(self, s, t):
        s_list = list(s)
        t_list = list(t)
        for i in s_list:
            t_list.remove(i)
        return t_list[0]
```

## Solution 2
```
class Solution:
    def findTheDifference(self, s, t):
        r = list(set(t))
        result = ' '
        for i in r:
            if s.count(i) != t.count(i):
                result = i
                return result
```



