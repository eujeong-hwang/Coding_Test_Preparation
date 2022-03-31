# https://leetcode.com/problems/merge-sorted-array/


# 내 머리로 못 품.. discussion꺼 이해는 함.. 토요일에 안 보고 다시 풀어보기 !!
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        # 답은 return을 하는게 아닌데, 잘 돌아가고 mergesort 되었는지 확인하기 위해서
        # return 해봄!
        return nums1

wth1 = Solution()
print(wth1.merge(nums1 = [1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3))


## Two pointers를 이용한 답 - from the discussion
## https://www.geeksforgeeks.org/two-pointers-technique/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=m-1
        j=n-1
        k=m+n-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        if j>=0:
            nums1[:k+1]=nums2[:j+1]


# Merge Sort
#https://www.geeksforgeeks.org/merge-sort/


# sort 관련되서 이거 한 번 해봄
# from typing import List
# class Solution:
#     def sorting(self, nums: List[int]) -> List[int]:
#         if len(nums) != 0:
#             nums.sort()
#         return nums

# wth = Solution()
# print("Function1:", wth.sorting([4,5,6,7,1,3]))


# # https://www.programiz.com/python-programming/methods/list/sort

# # Example
# prime_numbers = [11, 3, 7, 5, 2]

# # sort the list
# prime_numbers.sort()
# print(prime_numbers)

# # Output: [2, 3, 5, 7, 11]