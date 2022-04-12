# https://leetcode.com/problems/binary-tree-postorder-traversal/

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        stack=[]
        while root or stack:
            while root:
                stack.append(root) # push nodes into the stack
                root=root.left if root.left else root.right
            root=stack.pop()
            result.append(root.val) #Deal with the root node whenever it is popped from stack
            if stack and stack[len(stack)-1].left==root: #check whether it has been traversed 
                root=stack[len(stack)-1].right
            else:
                root=None #Force to quit the loop
        return(result)