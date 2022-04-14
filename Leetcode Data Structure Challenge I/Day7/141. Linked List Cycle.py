#https://leetcode.com/problems/linked-list-cycle/

# 1)
# Using Floyd's Tortoise & Hare Algorithm, Two Pointers Technique
# Definition for singly-linked list.
# 58ms 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def __init__(self):
    #     self.head = None

    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head

        # while fast and fast.next is not null
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

# llist = Solution()
# llist.head = ListNode(3)
# llist.head.next = ListNode(2)
# llist.head.next.next = ListNode(0)
# llist.head.next.next.next = ListNode(-4)


# 2)
# 52ms
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:        
            curr = head

            while curr:
                if curr.val is None:
                    return True
                curr.val = None
                curr = curr.next
            return False


# 3)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Hash set
class Solution:
    def __init__(self):
        self.head = None
        self.next = None

    def hasCycle(self, head: ListNode) -> bool:
        s=set()
        while head is not None:
            if head not in s:
                s.add(head)
            else:
                return True
            head=head.next
        return False

## ....
# ??다시해보기.
# llist = Solution()
# llist.head = ListNode(1)
# e2 = ListNode(2)
# # e3 = ListNode(0)
# # e4 = ListNode(-4)

# llist.head.next = e2
# # e2.next = e3
# # e3.next = e4

# print(llist.hasCycle(llist))
