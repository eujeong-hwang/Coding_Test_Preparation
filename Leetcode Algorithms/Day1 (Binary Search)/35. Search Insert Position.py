# https://leetcode.com/problems/search-insert-position/
# Binary Search Algorithm

# 49ms
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums)-1
        
        while l <= r:
            mid=int((l+r)/2)
            if nums[mid] < target:
                l = mid+1
            else:
                if nums[mid]== target and nums[mid-1]!=target:
                    return mid
                else:
                    r = mid-1
        return l
   


# 51ms
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:  
        low = 0
        high = len(nums)-1
        res = 0

        if not nums:
            return res
        
        while low <= high:
            
            mid = low + (high-low)//2 #use // notation to get absolute value
            
            if mid == len(nums)-1 and nums[mid] < target:
                return len(nums)
            
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
                if mid + 1 < len(nums) and nums[mid+1] > target:
                    res = mid + 1
                else:
                    res = mid
            else:
                high = mid - 1
                if mid - 1 > 0 and nums[mid-1] > target:
                    res = mid - 1
                else:
                    res = mid
                    
        return res


# https://leetcode.com/problems/search-insert-position/discuss/15378/A-fast-and-concise-python-solution-40ms-binary-search