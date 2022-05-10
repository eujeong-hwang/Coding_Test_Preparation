# https://leetcode.com/problems/n-th-tribonacci-number/

import collections
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = collections.defaultdict(int)
        memo[0], memo[1], memo[2] = 0,1,1
        for i in range(3,n+1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        return memo[n]