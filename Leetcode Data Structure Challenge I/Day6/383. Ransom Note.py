# https://leetcode.com/problems/ransom-note/

# 44ms
# counter하고 union 이용
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)
        
        return r&m == r

wth = Solution()
print(wth.canConstruct('aa', 'aab'))

# set 이용함
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         a = set(ransomNote) 
#         for i in a: 
#             if magazine.count(i) < ransomNote.count(i): 
#                 return False 
#         return True 