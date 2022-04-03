# ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ매우 느리다 ㅋㅋㅋㅋㅋㅋ 다른 6프로의 사람들보다 빠른 답 ㅋㅋㅋㅋㅋ레전드~
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []        
        if numRows < 1:
            return result
 
        for i in range(0, numRows):            
            row = []
            
            if i == 0:
                row.append(1)
            else:   
                row.insert(0, 1)
                row.insert(i, 1)
                
                for j in range(1, i):
                    left_above = result[i - 1][j  - 1]
                    right_above = result[i - 1][j]
                    row.insert(j, left_above + right_above)
            result.append(row)
        return result

# DP 이용했다고 한다.
# https://www.youtube.com/watch?v=vYquumk4nWw
# https://www.youtube.com/watch?v=oBt53YbR9Kk
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[0]*numRows
        for i in range(numRows):
            l[i]=[0]*(i+1)
            l[i][0]=1
            l[i][i]=1
            for j in range(1,i):
                l[i][j]=l[i-1][j-1]+l[i-1][j]
        return l


# What I learned

# [0]*numRows ->  [0] * x creates a list with x elements
# For example
 
[ 0 ] * 5
# output
[0, 0, 0, 0, 0]