# https://leetcode.com/problems/delete-and-earn/

class Solution(object):
    def rob(self, nums):
        prev = curr = 0
        for value in nums:
            prev, curr = curr, max(prev + value, curr)
        return curr

    def deleteAndEarn(self, nums):
        points = [0] * 10001
        for num in nums:
            points[num] += num
        return self.rob(points)