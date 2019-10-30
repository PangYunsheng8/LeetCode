# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        res = []
        
        def bfs(root, depth):
            if not root: return 
            
            if not root.left and not root.right: res.append(depth)
        
            bfs(root.left, depth+1)
            bfs(root.right, depth+1)
            
        bfs(root, 1)
            
        return min(res)
    
        