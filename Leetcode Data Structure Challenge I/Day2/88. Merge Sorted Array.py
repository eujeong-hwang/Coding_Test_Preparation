# https://leetcode.com/problems/merge-sorted-array/

from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        



from typing import List
class Solution:
    def sorting(self, nums: List[int]) -> List[int]:
        if len(nums) != 0:
            nums.sort()
        return nums

wth = Solution()
print("Function1:", wth.sorting([4,5,6,7,1,3]))


# https://www.programiz.com/python-programming/methods/list/sort

# Example
prime_numbers = [11, 3, 7, 5, 2]

# sort the list
prime_numbers.sort()
print(prime_numbers)

# Output: [2, 3, 5, 7, 11]