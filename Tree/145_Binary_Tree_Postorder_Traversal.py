# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 方法一：递归
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

# 方法二：迭代
class Solution1:
    def postorderTraversal(self, root: TreeNode):
        if not root: return
        
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            
            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)
        
        return res[::-1]