# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# 이것도 discussion에서 가져옴 -> 이해함 -> 근데 속도 매우 느림. 왜 느리지
# from typing import List
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         result = []
#         for i in nums1:
#             if i in nums2 and i not in result:
#                 result += [i]*min(nums1.count(i), nums2.count(i))
#         return result

# 이건 빠름. 근데 위에 코드가 더 이해하기 편하고 코드도 더 간단한거 같은데 ㅜㅜ 속도가 거의 2배로 빠름
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        one=0
        two=0
        
        ans=[]
        while one < len(nums1) and two < len(nums2):  
            if nums1[one] < nums2[two]:
                one+=1
            elif nums2[two] < nums1[one]:
                two+=1
            else:
                ans.append(nums1[one])
                one+=1
                two+=1
        return ans

# min(a,b) function in python
# https://thepythonguru.com/python-builtin-functions/min/
# 외우기    
min("abcDEF") # find smallest item in the string
'D' # 응?왜 D지?...

min([2, -1, 4, 3]) # find smallest item in the list
-1

min(("one", "two", "three")) # find smallest item in the tuple
'one'

min({1: "one", 2: "two", 3: "three"}) # find smallest item in the dict
1