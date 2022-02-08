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
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        answer = []
        
        while stack :
            node = stack.pop()
            if node :
                stack.append(node.right)
                stack.append(node)
                stack.append(node.left)
            else :
                if stack :
                    node = stack.pop()
                    answer.append(node.val)
                    
        return answer
```
