## Question - 1. Two Sum
https://leetcode.com/problems/two-sum/solution/

## Solution - Using Python3

- What is the difference between Python vs. Python3?

    Python 3 is more in-demand and includes a typing system. Python 2 is outdated and uses an older syntax for the print function. While Python 2 is still in use for configuration management in DevOps, Python 3 is the current standard.

1. Brute Force Algorithm

- What is Brute Force Algorithm? 

Trying all possible candidate solutions until the correct solution to the problem is found.

- How to solve this question using Brute Force Algorithm?

Loop through each element "x" and find if there is another value that equals to "target-x"

- The code
```
class Solution:
    def twoSum(self, nums = List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
```

- Time Complexity : O(n^2)

For each element, we try to find its complement by looping through the rest of the array which takes O(n) time.

- Space Complexity: O(1)

The space required does not depend on the size of the input array, so only constant space is used.