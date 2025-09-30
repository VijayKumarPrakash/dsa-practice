import numpy as np
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(bfs):
    if not bfs:
        return None
    
    root = TreeNode(bfs[0])
    queue = deque([root])
    i = 1
    n = len(bfs)
    
    while queue and i < n:
        current = queue.popleft()
        
        if bfs[i] is not None:
            current.left = TreeNode(bfs[i])
            queue.append(current.left)
        i += 1
        
        if i < n and bfs[i] is not None:
            current.right = TreeNode(bfs[i])
            queue.append(current.right)
        i += 1
    
    return root

def display(root):
    print(root.val)
    if root.left:
        display(root.left)
    if root.right:
        display(root.right)

def verticalTraversal(root, row=0, col=0, mat={}):
    if col not in mat:
        mat[col] = [root.val]
    else:
        mat[col].append(root.val)
    
    if root.left:
        verticalTraversal(root.left, row+1, col-1, mat)
    if root.right:
        verticalTraversal(root.right, row+1, col+1, mat)

    return mat


# Input 1
# input = [3,9,20,np.NAN,np.NAN,15,7]
# nodes = build_tree(input)

# Input 2
# input = [1,2,3,4,5,6,7]
# nodes = build_tree(input)

# Input 3
input = [8,2,3,4,6,5,7]
# Expected Output: [[4],[2],[8,5,6],[3],[7]]
nodes = build_tree(input)

# Input Vikram
# input = [3,1,4,0,2,2]
# nodes = build_tree(input)

vertical_traversal = verticalTraversal(nodes, 0, 0, {})

keys = vertical_traversal.keys()
for k in sorted(keys):
    print(vertical_traversal[k])
