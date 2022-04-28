# April 18, 2022
# Algorithms Daily Challenge - Day2
# Two Pointers Algorithm

# Did not use two pointers algorithm, used too much memory 
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = []
        for i in range(len(nums)):
            print(nums[i])
            squared.append(nums[i]*nums[i])
        
        return sorted(squared)
            
s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))

# Two Pointers Algorithm - 위에랑 시간은 별 차이 안나지만 memory가 16.5mb->16.2mb
class Solution:  
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = [None] * len(A)
        left, right = 0, len(A) - 1
        for index in range(len(A)-1, -1, -1):
            if abs(A[left]) > abs(A[right]):
                result[index] = A[left] ** 2
                left += 1
            else:
                result[index] = A[right] ** 2
                right -= 1
        return result

# range(len(A)-1, -1, -1)
# range([start], stop, [step])

# ex)
range(4,-1,-1)     # output: 4,3,2,1,0 