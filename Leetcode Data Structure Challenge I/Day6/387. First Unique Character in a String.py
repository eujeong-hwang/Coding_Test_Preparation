# https://leetcode.com/problems/first-unique-character-in-a-string/

# 연습해봄
from collections import Counter
a = "abcdefg"
m = Counter(a)
print("a : ", m.items())
print("index of c : ", a.index("c"))
# for i, j in m.items():
#     if i == 'd':    
#         print("True")
#     else:
#         print("False")

# Counter 사용
# 99 ms
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = Counter(s) # m: Counter({'a':2, 'b':2, 'c':1})
        for i,j in m.items(): # first for loop -> i:a, j:2
    	    if j == 1: 
                return(s.index(i))
    	
        return -1

wth = Solution()
print(wth.firstUniqChar("aabbc"))


# Hash Table 사용
# 134ms
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_table = {}
        
        for i in s:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1

        print("h", hash_table)

        for i in range(len(s)):
            if hash_table[s[i]] == 1:
                return i
        return -1
        
wth2 = Solution()
print(wth2.firstUniqChar('yhoyo'))

## 단어 나누기
# 1) split()
# 2) Typecasting to list
# https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
s = 'hello'    
l = list(s)
print(l)