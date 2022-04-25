# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# April 25, 2022

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        f= s = head
        # just want the loop, not the variable
        for _ in range(n):
            f = f.next
        if not f:
            return head.next
        while f.next:
            f = f.next
            s = s.next
        s.next = s.next.next
        return head