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

# 方法二：迭代
class Solution1:
    def inorderTraversal(self, root: TreeNode):
        res = []
        stack = []
        
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res