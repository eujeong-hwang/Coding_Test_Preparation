# April 18, 2022
# Algorithms Daily Challenge - Day2
# Two Pointers Algorithm

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """         
        def twopt(arr, i, j):
            while (i < j):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            return arr
        
        if k > len(nums):
            k %= len(nums)
            
        if (k > 0):
            twopt(nums, 0, len(nums) - 1)  # rotate entire array
            twopt(nums, 0, k - 1)          # rotate array upto k elements
            twopt(nums, k, len(nums) - 1)  # rotate array from k to end of array

r = Solution()
print(r.rotate([1,2,3,4,5,6,7], 3))