# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 方法一：递归
class Solution:
    def inorderTraversal(self, root: TreeNode):
        res = []
        
        def _inorderTraversal(root):
            if not root:
                return
            
            _inorderTraversal(root.left)
            res.append(root.val)
            _inorderTraversal(root.right)
        _inorderTraversal(root)
        
        return res