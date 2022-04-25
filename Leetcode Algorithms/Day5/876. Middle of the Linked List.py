# https://leetcode.com/problems/middle-of-the-linked-list/
# April 25, 2022

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Two pointer technique
# 27ms
class Solution:
    def middleNode(self, head:ListNode) -> ListNode:
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next

        return s