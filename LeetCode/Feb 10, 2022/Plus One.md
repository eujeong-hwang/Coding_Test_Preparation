# Feb 10, 2022
## Question - 66. Plus One
https://leetcode.com/problems/plus-one/

## Related Topics
    Array
    Math

## Question

    You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.

## Example

    # Input: digits = [1,2,3]
    # Output: [1,2,4]
    # Explanation: The array represents the integer 123.
                   Incrementing by one gives 123 + 1 = 124.
                   Thus, the result should be [1,2,4].


## Solution 1 
```
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        s = len(digits) - 1
        for i in digits:
            n += i * 10 ** s
            s -= 1
        return list(str(n + 1))
```

## Solution 2
```
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    
        digits = list(map(str, digits))
        nums = int(''.join(digits))
        nums += 1
        nums = list(str(nums))
        return list(map(int, nums))

s = Solution()
print(s.plusOne([1,2,3]))
```

## What I learned - Python map() function

https://www.w3schools.com/python/ref_func_map.asp