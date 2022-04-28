# https://leetcode.com/problems/flood-fill/
# April 27, 2022

from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        r, c = len(image), len(image[0])
        color = image[sr][sc]
        def dfs(i, j):
            if i < 0 or i>=r or j < 0 or j >= c:
                return
            if image[i][j] == newColor or image[i][j] != color:
                return
            image[i][j] = newColor
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i,j+1)
            dfs(i, j-1)
        dfs(sr, sc)
        return image