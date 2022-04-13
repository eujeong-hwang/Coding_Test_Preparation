# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 혼자 linked list 개념 안 쓰고 이런거나 하고 있었다;;
# from typing import Optional
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         final_table = []
        
#         for i in range(len(l1)):
#             for j in range(len(l2)):
#                 if l1[i] + l2[j] > 9 :
#                     final_table[i] = 0
#                     final_table[i+1] +=1

#                 elif l1[i] + l2[j] <= 9:
#                     final_table[i] = l1[i] + l2[j]

#         return final_table

# two_num = Solution()
# print(two_num.addTwoNumbers([2,4,3], [5,6,4]))                


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode()
        carry = 0
        while l1 or l2:
            v1, v2 = 0, 0
            if l1: v1, l1 = l1.val, l1.next
            if l2: v2, l2 = l2.val, l2.next
            
            val = carry + v1 + v2
            res.next = ListNode(val%10)
            res, carry = res.next, val//10
            
        if carry:
            res.next = ListNode(carry)
            
        return dummy.next