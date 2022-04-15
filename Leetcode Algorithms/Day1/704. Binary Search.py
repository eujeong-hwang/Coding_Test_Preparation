# https://leetcode.com/study-plan/algorithm/
# https://leetcode.com/problems/binary-search/
# Binary Search Algorithm

# Time Limit Exceeded ...:(
from typing import List
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         table = {}
#         while nums:
#             for i in range(len(nums)):
#                 table[nums[i]] = i
#                 if target in table:
#                     return i
#         return -1

# Binary Search
# Runtime: 250ms, Memory : 15.6MB
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = int(low + (high - low)/2)
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

bs = Solution()
print(bs.search([-1,0,3,5,9,12], 9))