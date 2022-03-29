# https://leetcode.com/problems/contains-duplicate/

# 최종 답
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for i in range(len(nums)):
            if nums[i] in duplicate:
                return True
            else:
                if nums[i] not in duplicate:
                    duplicate[nums[i]] = 1
        return False

wth = Solution()
print(wth.containsDuplicate([3,3]))


# 처음 답  --> 그냥 오답
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         duplicate = []
#         while nums != 0:
#             for i in nums:
#                 duplicate[i] = nums[i]
#                 for s in duplicate:
#                     if nums[i] in duplicate:
#                         return True
#                     else:
#                         return False


# 두 번째 답 --> 몇 개의 test case는 돌아가는데, [3,3]에서 wrong answer가 뜸. 왜인지 봤더니 duplicate은 
# dictionary인대, key value를 고려하지 않고 nums의 수를 집어 넣음.
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         duplicate = {}
#         for i in range(len(nums)):
#             if nums[i] in duplicate:
#                 return True
#             elif nums[i] not in duplicate:
#                 duplicate[i] = nums[i]
#         return False


## 이건 간단한 방법. set의 성질을 이용해 간단하게 한듯. (Discussion에서 가져옴)
class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))