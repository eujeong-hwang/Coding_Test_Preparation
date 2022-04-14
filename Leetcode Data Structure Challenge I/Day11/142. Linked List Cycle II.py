# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/
# https://leetcode.com/problems/linked-list-cycle-ii/

# Using Two-pointer technique instead of hash table

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# head = [3,2,0,-4]
# slow = fast = head = 3
# slow = 2, fast = 0
# slow = 0, fast = 2
# slow = -4, fast = -4 # slow == fast

# slow = head = 3, fast = -4
# while slow!= fast
    # slow = 2, fast = 2 
    # slow = 0, fast = -4
    # slow = -4, fast = 0
    # slow = 2, fast = 2  
        # return slow 
        # Tail connects to node index 1
        # There is a cycle in the linked list, where tail connects to the second node.

# 47ms
from typing import Optional
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        
        return None


