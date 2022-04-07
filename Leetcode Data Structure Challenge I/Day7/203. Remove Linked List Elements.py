# https://leetcode.com/problems/remove-linked-list-elements/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 72 ms
class Solution:
    def removeElements(self, head: Optional[ListNode], T: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = dummy
        while head:
            if head.val != T:
                prev = head
            else:
                prev.next = head.next
            head = head.next
        return dummy.next