# https://leetcode.com/problems/first-bad-version/
# Binary Search Algorithm

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# 27ms
class Solution:
    def firstBadVersion(self, n: int) -> int:
        r = n-1
        l = 0
        while(l<=r):
            mid = int(l + (r-l)/2)
            if isBadVersion(mid)==False:
                l = mid+1
            else:
                r = mid-1
        return l
        