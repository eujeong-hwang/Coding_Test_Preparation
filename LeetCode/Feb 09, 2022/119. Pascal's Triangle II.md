# Feb 09, 2022
## Question - 119. Pascals Triangle II
https://leetcode.com/problems/pascals-triangle-ii/

## Related Topics
    Array
    Dynamic Programming

## What is Dynamic Programming?

https://github.com/eujeong-hwang/Coding_Test_Preparation/blob/main/Concepts/Algorithm/Dynamic%20Programming.md

## Question

    Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

![PascalTriangleAnimated2](https://user-images.githubusercontent.com/59908525/153146793-77bcba2e-610f-4edd-81f8-261dfbbdfe4f.gif)

## Solution 1 
```
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                result[i - j] += result[i - j - 1]
        return result


if __name__ == "__main__":
    assert Solution().getRow(3) == [1, 3, 3, 1]
```

## Solution 2
```
class Solution(object):
    def getRow(self, rowIndex):
        result = []
        
        for i in range(0, rowIndex+1):
            result.append([])
            
            for j in range(0, i + 1):
                if j == 0:
                    result[i].append(1)
                elif i == j:
                    result[i].append(1)
                else:
                    result[i].append((result[i-1][j-1]) + (result[i-1][j]))
                    
        
        return result[rowIndex]
```