# https://leetcode.com/problems/valid-sudoku/

# ****Set cannot have duplicates ***** -> This is the reason why we are using set as a defaultdict
from collections import defaultdict
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_bag = defaultdict(set)
        col_bag = defaultdict(set)
        sec_bag = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if not num.isdigit():
                    continue

                sec = (i // 3, j // 3)
                if num in row_bag[i] or num in col_bag[j] or num in sec_bag[sec]:
                    return False
                else:
                    row_bag[i].add(num)
                    col_bag[j].add(num)
                    sec_bag[sec].add(num)
        return True

# 느림..!
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         rows = [set() for i in range(9)]
#         cols = [set() for i in range(9)]
#         mMat = [set() for i in range(9)]
        
#         for i in range(9):
#             for j in range(9):
#                 cur = board[i][j]
#                 if cur != '.':
                    
#                     k = (i // 3 ) * 3 + j // 3
                
#                     if cur not in rows[i]: rows[i].add(cur)
#                     else: return False
                    
#                     if cur not in cols[j]: cols[j].add(cur)
#                     else: return False
                
#                     if cur not in mMat[k]: mMat[k].add(cur)
#                     else: return False
#         return True

#----------------------------------------------------------------------------------------------------#

# What I learned

# 1) Python Collections
# https://docs.python.org/3/library/collections.html
# defaultdict -> https://docs.python.org/3/library/collections.html#defaultdict-objects

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print('d', d) # defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})
print('here', sorted(d.items())) # 알파벳 순으로 sorted()
                                 # [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

#--------------------------------------------------------------------------------------------#
# 2) sorted()
# https://www.w3schools.com/python/ref_func_sorted.asp
a = [('b', [3,4]), ('a', [1,2]), ('d', [6,7])]
print('here2', sorted(a)) # [('a', [1, 2]), ('b', [3, 4]), ('d', [6, 7])]

#--------------------------------------------------------------------------------------------#
# 3) Characteristics of SET 

# 1- set cannot have duplicates
# Output: {1, 2, 3, 4}
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# 2- we can make set from a list
# Output: {1, 2, 3}
my_set = set([1, 2, 3, 2])
print(my_set) #output: {1, 2, 3}

# 3- set cannot have mutable items
# here [3, 4] is a mutable list
# this will cause an error.
my_set = {1, 2, [3, 4]}

#--------------------------------------------------------------------------------------------# 
# 4) What is [x for x in range(10)]??
# It's a List Comprehension Method

# example)
# create a list using list comprehension
squares = [x**2 for x in range(10)]
print(squares)

# Same as this example)
squares = []
for x in range(10):
    # raise x to the power of 2
    squares.append(x**2)
print(squares)