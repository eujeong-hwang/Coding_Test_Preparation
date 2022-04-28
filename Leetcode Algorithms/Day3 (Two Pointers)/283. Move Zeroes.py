# https://leetcode.com/problems/move-zeroes/


from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1) First Attempt
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         if nums[len(nums)-1] != 0:
        #             nums[i] = nums[len(nums)-1]
        #             nums[len(nums)-1] = 0
        #         elif nums[len(nums)-1] == 0:
        #             nums[i] = nums[len(nums)-2]
        #             nums[len(nums)-2] = 0

        # 2) 2nd Attempt
        # def twopt(arr, i, j):
        #     while (i < j):
        #         arr[i], arr[j] = arr[j], arr[i]
        #         i += 1
        #         j -= 1
        #     return arr
        
        # if k > len(nums):
        #     k %= len(nums)
            
        # if (k > 0):
        #     twopt(nums, 0, len(nums) - 1)  # move zeroes to the end
        #     twopt(nums, 0, k - 1)          # sort the nums before 0
        
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1
tp = Solution()
print(tp.moveZeroes([0,3,0,1,12]))
