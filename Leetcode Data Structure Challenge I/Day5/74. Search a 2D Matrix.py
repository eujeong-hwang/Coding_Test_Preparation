# https://leetcode.com/problems/search-a-2d-matrix/

# 풀이
# https://leetcode.com/problems/search-a-2d-matrix/discuss/896821/Python-Simple-binary-search-explained
from typing import List
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: 
            return False
        m, n = len(matrix[0]), len(matrix)
        beg, end = 0, m*n - 1
        while beg < end:
            mid = (beg + end)//2
            if matrix[mid//m][mid%m] < target:
                beg = mid + 1
            else:
                end = mid
        return matrix[beg//m][beg%m] == target

wth = Solution()
print("1. ", wth.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print("2. ", wth.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))

#-----------------------------------------------------------------------------#
# Binary Search
# https://www.geeksforgeeks.org/python-program-for-binary-search/