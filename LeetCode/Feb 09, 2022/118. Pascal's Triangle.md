# Feb 09, 2022
## Question - 118. Pascals Triangle
https://leetcode.com/problems/pascals-triangle/

## Related Topics
    Array
    Dynamic Programming

## What is Dynamic Programming?

https://github.com/eujeong-hwang/Coding_Test_Preparation/blob/main/Concepts/Algorithm/Dynamic%20Programming.md

## Question

    Given an integer numRows, return the first numRows of Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

![PascalTriangleAnimated2](https://user-images.githubusercontent.com/59908525/153146793-77bcba2e-610f-4edd-81f8-261dfbbdfe4f.gif)

## Solution 1 
```
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
```
