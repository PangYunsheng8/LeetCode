# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        if not root: return True
        left = self.depth(root.left)
        right = self.depth(root.right)
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

        # 获取某一个结点的最大深度
    def depth(self, root):
        if not root: return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))