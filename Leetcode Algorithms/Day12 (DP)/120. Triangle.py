# 3
# https://leetcode.com/problems/triangle/

from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        f = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i in range(len(row)):
                f[i] = row[i] + min(f[i], f[i + 1])
        return f[0]