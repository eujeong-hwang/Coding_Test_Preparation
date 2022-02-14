# Feb 14, 2022
## Question - 100. Same Tree
https://leetcode.com/problems/same-tree/

## Related Topics
    Tree
    Depth-First Search
    Breadth-First Search
    Binary Tree


## Code
```
# Python program to determine if two trees are identical
 
# A binary tree node has data, pointer to left child
# and a pointer to right child
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
     
 
# Given two trees, return true if they are structurally
# identical
def identicalTrees(a, b):
     
    if a == None and b == None:
        return True
 
    if a == None or b == None:
        return False
    
    elif a.data == b.data:
        return identicalTrees(a.left, b.left) and identicalTrees(a.right, b.right)
    
    return False
# Driver program to test identicalTress function
root1 = Node(1)
root2 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
 
root2.left = Node(2)
root2.right = Node(4)
root2.left.left = Node(5)
root2.left.right = Node(6)
 
if identicalTrees(root1, root2):
    print("Both trees are identical")
else:
    print ("Trees are not identical")
```

### Debugging Process
<img width="667" alt="debuggingggg" src="https://user-images.githubusercontent.com/59908525/153883873-29fde42d-b23b-4d07-bbb5-4fb44b2cf8e8.PNG">

