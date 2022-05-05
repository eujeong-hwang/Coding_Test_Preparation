# 2
# https://leetcode.com/problems/number-of-1-bits/

# https://leetcode.com/problems/number-of-1-bits/discuss/55106/Python-2-solutions.-One-naive-solution-with-built-in-functions.-One-trick-with-bit-operation

# 35ms
class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c

# using built-in function
# 60ms
class Solution:
    def hammingWeight(self, n: int) -> int:    
        return bin(n).count('1')