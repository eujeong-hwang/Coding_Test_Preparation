# https://leetcode.com/problems/valid-anagram/

# 57ms
# 해냈다..
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            hash_table = {}
            
            for i in s:
                if i not in hash_table: 
                    hash_table[i] = 1
                else:
                    hash_table[i] += 1
            for i in t:
                if i in hash_table:
                    hash_table[i] -= 1
                else:
                    return False

            for b,c in hash_table.items():
                if c!=0:
                    return False
            return True
        
p = Solution()
print(p.isAnagram("rat", "car")) # False
print(p.isAnagram("aaa", "a")) # False
print(p.isAnagram("anagram", "nagaram")) #True  