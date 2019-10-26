# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 方法一：递归
class Solution:
    def preorderTraversal(self, root: TreeNode):
        res = []
        
        def _preorderTraversal(root):
            if not root:
                return 
            
            res.append(root.val)
            _preorderTraversal(root.left)
            _preorderTraversal(root.right)
        
        _preorderTraversal(root)
        
        return res