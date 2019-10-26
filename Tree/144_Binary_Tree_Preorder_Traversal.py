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

# 方法二：迭代
class Solution1:
    def preorderTraversal(self, root: TreeNode):
        if not root: return []
        
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            
            if node.right:
                stack.append(node.right)
                
            if node.left:
                stack.append(node.left)
        
        return res