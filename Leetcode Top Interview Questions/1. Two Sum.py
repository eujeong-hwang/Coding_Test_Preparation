# https://leetcode.com/problems/two-sum/

from typing import List
class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        hash_table = {}

        for i in range(len(nums)):
            hash_table[nums[i]] = i
        for j in range(len(nums)):
            otherNum = target - nums[j]
            if otherNum in hash_table and otherNum != j:
                return [j, hash_table[otherNum]]

