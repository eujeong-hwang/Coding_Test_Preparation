# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        else:
            prev1 = 1
            prev2 = 2

            for i in range(3, n+1):
                cur = prev1 + prev2
                prev1, prev2 = prev2, cur
            
            return cur