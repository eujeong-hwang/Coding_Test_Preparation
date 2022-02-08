# Feb 08, 2022
## Question - 144. Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/

## Related Topics
    Stack
    Tree
    Depth-First Search
    Binary Tree

## What is Binary Tree Traversals (Inorder, Preorder and Postoder)

    Unlike linear data structures (Array, Linked List, Queues, Stacks, etc) which have only one logical way to traverse them, 
    trees can be traversed in different ways. Following are the generally used ways for traversing trees.

<img width="800" alt="Binary Tree" src="https://user-images.githubusercontent.com/59908525/152982809-3b5f66ec-324e-4544-b72f-3a87267d4e22.PNG">

    Depth First Traversals:
    (a) Inorder (Left, Root, Right) : 4 2 5 1 3
    (b) Preorder (Root, Left, Right) : 1 2 4 5 3
    (c) Postorder (Left, Right, Root) : 4 5 2 3 1
    
    Breadth-First or Level Order Traversal: 1 2 3 4 5

    https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
    https://github.com/eujeong-hwang/Coding_Test_Preparation/blob/main/LeetCode/Feb%2008%2C%202022/Binary%20Tree%20Inorder%20Traversal.md

## Solution 1 - Iteratively - Using Python3

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        S = [root]
        rtn = []
        while S:
            N = S.pop()
            # Visit the node first
            rtn.append(N.val)
            # Push right child first which will be traversed last
            if N.right:
                S.append(N.right)
            # Then push left child which will be traverse earlier
            if N.left:
                S.append(N.left)

        return rtn
```

## Solution 2 - Recursive - Using Python3

```
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        self.rtn = []
        self.helper(root)
        return self.rtn

    def helper(self, node):
        self.rtn.append(node.val)
        # Then traverse left child
        if node.left:
            self.helper(node.left)
        # Traverse right child at last
        if node.right:
            self.helper(node.right)
```