# https://leetcode.com/problems/letter-case-permutation/

from typing import List
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = ['']
        for ch in s:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i+ch for i in res]
        return res

# https://www.w3schools.com/python/ref_string_isalpha.asp