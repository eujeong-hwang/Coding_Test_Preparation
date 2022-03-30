# https://leetcode.com/problems/two-sum/

# Brute Force 방법 -> 매우..느림..!
# from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if target == nums[j] + nums[i]:
#                     return [i,j]    

# wth = Solution()
# print(wth.twoSum([3,3], 6))

# Using Hash Table
# Runtime이 위에 bruteforce 6972ms에서 89ms로 줄어듬 !
from typing import List
class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        hash_table = {}

        for i in range(len(nums)):
            hash_table[nums[i]] = i
        for j in range(len(nums)):
            whereAreYou = target - nums[j]
            if whereAreYou in hash_table and hash_table[whereAreYou] != j:
                return [j, hash_table[whereAreYou]]

wth = Solution()
print(wth.twoSum([1,3,4,5], 7))

            