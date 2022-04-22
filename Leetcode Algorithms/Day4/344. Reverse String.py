# https://leetcode.com/problems/reverse-string/
# Arpil 22, 2022

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start,end = 0, len(s)-1
        while start <=end:
            s[start],s[end]=s[end],s[start]
            start+=1
            end-=1
