# https://leetcode.com/problems/maximum-subarray/

# Discussion에서 가져옴. [0]이 뭐지..?
# from typing import List
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         dp = [0]*len(nums)
#         dp[0] = nums[0]
#         for i in range(1, len(nums)):
#             dp[i] = max(dp[i-1]+nums[i], nums[i])
#         return max(dp)

# Easy인 문제인대 아직 내 머리로 divide conquer, dynamic programming 하는 문제는 접근부터 못하겠다..ㄸㄹㄹ
# 그래도 이 문제는 이해했다.. 외워야지.. 다음에 비슷한거 나오면 그대로 해야지..
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        return maxSum

wth = Solution()
print(wth.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))