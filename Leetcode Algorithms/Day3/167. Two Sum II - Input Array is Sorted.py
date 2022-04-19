# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


# Zero-based array indexing is a way of numbering the items in an array 
# such that the first item of it has an index of 0,
# whereas a one-based array indexed array has its first item indexed as 1
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1
 
t = Solution()
print(t.twoSum([2,7,11,15], 9))