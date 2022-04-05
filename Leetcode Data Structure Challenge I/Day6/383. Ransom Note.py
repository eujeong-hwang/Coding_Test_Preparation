# https://leetcode.com/problems/ransom-note/

# from collections import Counter
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         r = Counter(ransomNote)
#         m = Counter(magazine)
        
#         return r&m == ransomNote

# wth = Solution()
# print(wth.canConstruct('a', 'b'))
# --> 이거 안됨. 왜냐하면

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         a = set(ransomNote) 
#         for i in a: 
#             if magazine.count(i) < ransomNote.count(i): 
#                 return False 
#         return True 