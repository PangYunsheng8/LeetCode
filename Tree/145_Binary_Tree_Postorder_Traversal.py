# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode):
        res = []
        
        def _postorderTraversal(root):
            if not root:
                return 
            
            _postorderTraversal(root.left)
            _postorderTraversal(root.right)
            res.append(root.val)
        
        _postorderTraversal(root)
        
        return res