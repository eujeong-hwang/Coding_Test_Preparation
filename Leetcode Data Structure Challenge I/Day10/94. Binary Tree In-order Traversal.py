# https://leetcode.com/problems/binary-tree-inorder-traversal/


from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# (a) Inorder (Left, Root, Right)
# iteratively
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

# recursive 
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.helper(root, result)
        return result
    
    
    def helper(self, root, result):
        if root == None:
            return
        
        self.helper(root.left, result)
        result.append(root.val)
        self.helper(root.right, result)

# 이것도 참고하기
# https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/713539/Python-3-All-Iterative-Traversals-InOrder-PreOrder-PostOrder-Similar-Solutions