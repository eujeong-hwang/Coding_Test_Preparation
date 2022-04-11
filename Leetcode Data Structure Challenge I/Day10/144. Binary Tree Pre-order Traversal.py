# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Depth First Traversals:
#     (a) Inorder (Left, Root, Right) : 4 2 5 1 3
#     (b) Preorder (Root, Left, Right) : 1 2 4 5 3
#     (c) Postorder (Left, Right, Root) : 4 5 2 3 1
#     Breadth-First or Level Order Traversal: 1 2 3 4 5


from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        pass

