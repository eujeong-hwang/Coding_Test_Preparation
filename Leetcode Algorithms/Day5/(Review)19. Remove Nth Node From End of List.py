# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# April 25, 2022

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# without dummy
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

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = dummy = ListNode(0)
        dummy.next = head
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next